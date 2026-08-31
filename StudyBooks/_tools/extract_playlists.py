#!/usr/bin/env python3
"""
extract_playlists.py
--------------------------------------------------------------------
Extracts every video (title, description, duration, link) from the
YouTube playlists chosen for each Sem-3 subject, then auto-matches
each video to the syllabus topics (same keyword system used in
detect_topics.py).

OUTPUT (in extracted_json/video_maps/):
  <Subject>_videos.json     - every video with full details
  <Subject>_topic_videos.json - syllabus topic -> matching videos
  _index.json               - summary of all playlists processed

--------------------------------------------------------------------
SETUP (once):
    pip3 install yt-dlp
    (no API key needed - yt-dlp reads public playlist metadata)

USAGE:
    python3 extract_playlists.py            # all subjects
    python3 extract_playlists.py Maths      # only playlists whose
                                            # subject name contains "Maths"
--------------------------------------------------------------------
NOTE: fetching full descriptions requires one metadata request per
video, so a 100-video playlist takes a few minutes. A fast first pass
(--flat) grabs titles/links only:
    python3 extract_playlists.py --flat
"""

import os, re, sys, json, subprocess
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "extracted_json", "video_maps")
os.makedirs(OUT, exist_ok=True)

# -------------------------------------------------------------------
# The playlists you selected (subject -> list of playlists)
# -------------------------------------------------------------------
PLAYLISTS = {
    "Mathematics-III": [
        ("Tending To Infinity — BSC-301 playlist",
         "https://youtube.com/playlist?list=PLn3Wz38keZOfactXksvsD2LDc8wpVBiaA"),
    ],
    "Data_Structure_Algorithm": [
        ("Gate Smashers — DSA playlist",
         "https://youtube.com/playlist?list=PLxCzCOWd7aiEwaANNt3OqJPVIxwp2ebiT"),
    ],
    "Computer_Organization": [
        ("Gate Smashers — COA playlist",
         "https://youtube.com/playlist?list=PLxCzCOWd7aiHMonh3G6QNKq53C6oNXGrX"),
    ],
    "Analog_and_Digital_Electronics": [
        ("Neso Academy — Analog Electronics playlist",
         "https://youtube.com/playlist?list=PLBlnK6fEyqRiw-GZRqfnlVIBz9dxrqHJS"),
        ("Neso Academy — Digital Electronics playlist",
         "https://youtube.com/playlist?list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm"),
    ],
    # Economics: no playlist chosen (organizer-based prep). Add here if found later.
}

# -------------------------------------------------------------------
# Syllabus topics with match keywords (subject -> topic -> keywords).
# Keywords are matched (case-insensitive) against title + description.
# -------------------------------------------------------------------
TOPICS = {
    "Mathematics-III": {
        "Unit1: Sequences & series convergence": ["sequence", "series", "convergen", "diverg", "ratio test", "root test", "comparison test", "p-series", "alternating", "leibnitz", "leibniz", "cauchy"],
        "Unit1: Power/Taylor series": ["power series", "taylor", "maclaurin", "expansion"],
        "Unit2: Partial derivatives & Euler": ["partial deriv", "euler", "homogeneous", "chain rule", "implicit", "total deriv", "limit and continuity"],
        "Unit2: Jacobian": ["jacobian"],
        "Unit2: Maxima minima saddle": ["maxima", "minima", "saddle", "extrem", "lagrange"],
        "Unit2: Gradient divergence curl": ["gradient", "divergence", "curl", "directional deriv", "solenoidal", "irrotational", "vector"],
        "Unit3: Double & triple integrals": ["double integral", "triple integral", "multiple integral", "area by integration"],
        "Unit3: Change of order/variables, polar": ["change of order", "change the order", "polar", "change of variable"],
        "Unit3: Green Gauss Stokes": ["green", "gauss", "stoke", "divergence theorem", "line integral", "surface integral"],
        "Unit4: First order ODE (exact/linear/Bernoulli)": ["exact", "bernoulli", "integrating factor", "first order", "orthogonal trajector", "linear differential"],
        "Unit4: Higher degree p, Clairaut": ["clairaut", "solvable for p", "solvable for x", "solvable for y", "singular solution"],
        "Unit4: Second order, D-operator, variation, Cauchy-Euler": ["second order", "d operator", "d-operator", "particular integral", "complementary function", "variation of parameter", "cauchy euler", "cauchy-euler", "homogeneous linear"],
        "Unit5: Graph theory basics": ["graph", "euler graph", "hamiltonian", "walk", "path", "circuit", "degree", "digraph"],
        "Unit5: Incidence/adjacency matrix": ["adjacency", "incidence"],
        "Unit5: Trees, spanning, Kruskal, Prim": ["tree", "spanning", "kruskal", "prim"],
    },
    "Data_Structure_Algorithm": {
        "Complexity & asymptotic notation": ["time complexity", "asymptotic", "big o", "big-o", "omega", "theta", "space complexity"],
        "Arrays & searching": ["array", "linear search", "binary search"],
        "Stack & applications": ["stack", "infix", "postfix", "prefix", "expression"],
        "Queue types": ["queue", "circular queue", "priority queue", "deque"],
        "Linked lists": ["linked list", "doubly", "circular linked"],
        "Trees BST AVL B B+": ["binary tree", "bst", "binary search tree", "avl", "b tree", "b-tree", "b+ tree", "threaded", "traversal"],
        "Sorting": ["bubble", "selection sort", "insertion sort", "quick sort", "merge sort", "heap sort", "sorting"],
        "Hashing": ["hash", "collision"],
        "Graphs BFS DFS": ["graph", "bfs", "dfs", "breadth first", "depth first", "adjacency"],
    },
    "Computer_Organization": {
        "Unit1: Stored program, instruction cycle": ["von neumann", "instruction cycle", "fetch", "stored program", "functional unit", "computer organization introduction", "basic organization"],
        "Unit1: Instruction formats & addressing modes": ["addressing mode", "instruction format", "zero address", "one address", "two address", "three address"],
        "Unit2: Number representation & IEEE 754": ["ieee", "floating point", "fixed point", "2's complement", "number representation", "sign magnitude"],
        "Unit2: Adders (ripple/CLA) & ALU": ["adder", "carry look", "ripple carry", "alu"],
        "Unit2: Booth's multiplication": ["booth"],
        "Unit2: Division restoring/non-restoring": ["restoring", "division algorithm", "non restoring", "non-restoring"],
        "Unit3: Memory hierarchy & organization": ["memory hierarchy", "ram", "rom", "sram", "dram", "associative memory", "memory organization", "auxiliary"],
        "Unit3: Cache memory & mapping": ["cache", "direct mapping", "set associative", "fully associative", "write back", "write through", "hit ratio"],
        "Unit3: Virtual memory": ["virtual memory", "page", "paging", "tlb", "segmentation", "page fault", "page replacement"],
        "Unit4: Control unit design": ["control unit", "hardwired", "microprogrammed", "micro programmed", "microinstruction"],
        "Unit4: Pipelining": ["pipelin", "hazard"],
        "Unit4: RISC vs CISC": ["risc", "cisc"],
        "Unit4: I/O, interrupts, DMA": ["dma", "interrupt", "i/o", "input output", "handshak", "polling", "daisy", "bus arbitration", "asynchronous data transfer"],
    },
    "Analog_and_Digital_Electronics": {
        "Unit1: Amplifier classes & power amplifiers": ["class a", "class b", "class ab", "class c", "power amplifier", "push pull", "push-pull", "crossover", "efficiency"],
        "Unit1: Feedback & oscillators": ["feedback", "oscillator", "barkhausen", "wien", "phase shift"],
        "Unit1: Multivibrators, Schmitt, 555": ["multivibrator", "astable", "monostable", "bistable", "schmitt", "555"],
        "Unit2: Number systems & codes": ["number system", "binary", "octal", "hexadecimal", "bcd", "gray code", "excess-3", "excess 3", "ascii", "complement"],
        "Unit2: Boolean algebra & K-map": ["boolean", "de morgan", "demorgan", "k map", "k-map", "karnaugh", "sop", "pos", "minterm", "maxterm", "quine", "mccluskey"],
        "Unit2: Adders/subtractors": ["half adder", "full adder", "subtractor", "adder"],
        "Unit2: Encoder/decoder/MUX/comparator/parity": ["multiplexer", "mux", "demultiplexer", "decoder", "encoder", "comparator", "parity"],
        "Unit3: Flip-flops & latches": ["flip flop", "flip-flop", "latch", "sr ", "jk ", "d flip", "t flip", "master slave", "race around", "race-around"],
        "Unit3: Registers": ["register", "siso", "sipo", "piso", "pipo", "shift register"],
        "Unit3: Counters": ["counter", "ripple counter", "synchronous counter", "asynchronous counter", "ring counter", "johnson", "mod-"],
        "Unit4: DAC/ADC": ["dac", "adc", "digital to analog", "analog to digital", "r-2r", "successive approximation", "flash type", "dual slope"],
        "Unit4: Logic families": ["ttl", "ecl", "cmos", "logic family", "logic families", "fan out", "fan-out", "noise margin", "propagation delay"],
    },
}


def ytdlp_cmd():
    """Find a working yt-dlp invocation: the binary if on PATH,
    otherwise fall back to `python3 -m yt_dlp` (works whenever
    `pip3 install yt-dlp` succeeded, regardless of PATH)."""
    for cand in (["yt-dlp"], [sys.executable, "-m", "yt_dlp"]):
        try:
            subprocess.run(cand + ["--version"], capture_output=True, check=True)
            return cand
        except Exception:
            continue
    return None


YTDLP = None  # set in main()


def subject_matches(filter_str, subject):
    """Loose subject-name match: case-insensitive, ignores underscores/
    hyphens/spaces, and tolerates a trailing 's' (so 'Maths' matches
    'Mathematics-III', 'Data' matches 'Data_Structure_Algorithm', etc.).
    A plain substring check fails for cases like 'maths' in 'mathematics'
    because 'maths' is not literally a substring of 'mathematics'."""
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower()).rstrip("s")
    f, s = norm(filter_str), norm(subject)
    return bool(f) and (f in s or s in f)


def fetch_playlist(url, flat=False):
    """Return a list of video dicts from a playlist via yt-dlp JSON output."""
    cmd = list(YTDLP) + ["--ignore-errors", "--no-warnings", "-J"]
    if flat:
        cmd.append("--flat-playlist")
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
    if not r.stdout.strip():
        raise RuntimeError(f"yt-dlp returned nothing for {url}\nstderr: {r.stderr[:500]}")
    data = json.loads(r.stdout)
    vids = []
    for e in data.get("entries") or []:
        if e is None:
            continue
        vid = e.get("id") or ""
        vids.append({
            "title": e.get("title") or "",
            "url": e.get("webpage_url") or (f"https://www.youtube.com/watch?v={vid}" if vid else ""),
            "duration_sec": e.get("duration"),
            "description": (e.get("description") or "")[:2000],
            "uploader": e.get("uploader") or e.get("channel") or "",
        })
    return vids


def match_topics(subject, videos):
    """topic -> [video, ...] using keyword hits on title+description."""
    topics = TOPICS.get(subject, {})
    result = {t: [] for t in topics}
    unmatched = []
    for v in videos:
        text = (v["title"] + " " + v["description"]).lower()
        hit_any = False
        for topic, keys in topics.items():
            if any(k in text for k in keys):
                result[topic].append({"title": v["title"], "url": v["url"],
                                      "duration_sec": v["duration_sec"]})
                hit_any = True
        if not hit_any:
            unmatched.append({"title": v["title"], "url": v["url"]})
    result["_unmatched (check manually)"] = unmatched
    return result


def main():
    args = [a for a in sys.argv[1:]]
    flat = "--flat" in args
    args = [a for a in args if not a.startswith("--")]
    subject_filter = args[0].lower() if args else None

    global YTDLP
    YTDLP = ytdlp_cmd()
    if YTDLP is None:
        sys.exit("yt-dlp not found. Install with:  pip3 install yt-dlp")
    print(f"using yt-dlp via: {' '.join(YTDLP)}")

    index = []
    for subject, pls in PLAYLISTS.items():
        if subject_filter and not subject_matches(subject_filter, subject):
            continue
        all_videos = []
        for name, url in pls:
            print(f"\n[{subject}] fetching: {name}")
            print(f"  {url}")
            try:
                vids = fetch_playlist(url, flat=flat)
            except Exception as e:
                print(f"  !! failed: {e}")
                continue
            print(f"  -> {len(vids)} videos")
            for v in vids:
                v["playlist"] = name
            all_videos.extend(vids)

        if not all_videos:
            continue

        vfile = os.path.join(OUT, f"{subject}_videos.json")
        with open(vfile, "w", encoding="utf-8") as f:
            json.dump({"subject": subject, "fetched_at": datetime.now().isoformat(timespec="seconds"),
                       "flat_mode": flat, "count": len(all_videos), "videos": all_videos},
                      f, ensure_ascii=False, indent=2)

        tmap = match_topics(subject, all_videos)
        tfile = os.path.join(OUT, f"{subject}_topic_videos.json")
        with open(tfile, "w", encoding="utf-8") as f:
            json.dump({"subject": subject, "topic_videos": tmap}, f, ensure_ascii=False, indent=2)

        matched = sum(len(v) for k, v in tmap.items() if not k.startswith("_"))
        print(f"  saved {os.path.basename(vfile)} + topic map "
              f"({matched} topic-matches, {len(tmap['_unmatched (check manually)'])} unmatched)")
        index.append({"subject": subject, "videos": len(all_videos),
                      "files": [os.path.basename(vfile), os.path.basename(tfile)]})

    with open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"\nDone. Output -> {OUT}")


if __name__ == "__main__":
    main()
