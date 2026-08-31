#!/usr/bin/env python3
"""
detect_topics.py
Maps each syllabus topic (per subject, per unit) to where it is covered
in BOTH source books. Produces one topic-map JSON per subject in
  extracted_json/topicmaps/<Subject>_topicmap.json

For each topic it records, for book1 and book2:
  - hit_count  : how many pages mention the topic
  - pages      : the page numbers (first 40) where it appears
  - verdict    : Strong / Partial / Weak / Missing coverage
This becomes the blueprint Fable 5 uses to author the study books.
"""
import os, re, json, glob

BASE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(BASE, "extracted_json")
OUT  = os.path.join(JDIR, "topicmaps")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------------------
# Syllabus -> units -> topics.  Each topic has search "keys" (regex-ish, all
# lowercased). A page counts as a hit if ANY key appears on it.
# ---------------------------------------------------------------------------
SYLLABUS = {
  "Analog_and_Digital_Electronics": {
    "book1": "Analog_and_Digital_Electronics_book1.json",
    "book2": "Analog_and_Digital_Electronics_book2.json",
    "units": {
      "Unit 1 - Analog": [
        ("Classes of amplifiers (A, B, AB, C)", ["class a amplifier","class b amplifier","class ab","class c amplifier","power amplifier"]),
        ("Amplifier power & efficiency",        ["amplifier efficiency","conversion efficiency","collector efficiency","maximum efficiency"]),
        ("Feedback concepts",                   ["negative feedback","positive feedback","feedback amplifier","barkhausen"]),
        ("Oscillators (Phase Shift, Wien)",     ["phase shift oscillator","wien bridge","wien-bridge","rc oscillator"]),
        ("Multivibrators (Astable/Monostable)", ["astable multivibrator","monostable multivibrator","multivibrator"]),
        ("Schmitt Trigger",                     ["schmitt trigger"]),
        ("555 Timer",                           ["555 timer","555 ic","ne555","timer ic"]),
      ],
      "Unit 2 - Number systems & Combinational": [
        ("Number systems & codes (BCD/Gray/ASCII)", ["binary number","bcd code","gray code","ascii","excess-3","excess 3","ebcdic"]),
        ("Signed numbers & 1's/2's complement", ["1's complement","2's complement","one's complement","two's complement","signed binary"]),
        ("Boolean algebra",                     ["boolean algebra","de morgan","demorgan","boolean function"]),
        ("SOP / POS & K-map minimization",      ["sum of products","product of sums","karnaugh","k-map","minterm","maxterm"]),
        ("Adders & Subtractors",                ["half adder","full adder","half subtractor","full subtractor","adder","subtractor","subtracter"]),
        ("Encoder/Decoder/MUX/DEMUX/Comparator/Parity", ["multiplexer","demultiplexer","decoder","encoder","comparator","parity generator"]),
      ],
      "Unit 3 - Sequential": [
        ("Flip-flops (SR/JK/D/T/Master-slave)", ["sr flip-flop","jk flip-flop","d flip-flop","t flip-flop","master-slave","master slave","latch"]),
        ("Registers (SISO/SIPO/PIPO/PISO)",     ["shift register","siso","sipo","pipo","piso"]),
        ("Counters (Ring/Johnson/Sync/Async/Mod-N)", ["ring counter","johnson counter","synchronous counter","asynchronous counter","ripple counter","mod-n","modulus counter"]),
      ],
      "Unit 4 - Converters & Logic families": [
        ("D/A conversion (R-2R)",               ["r-2r","digital to analog","dac","d/a converter","ladder network"]),
        ("A/D conversion (successive approx.)", ["successive approximation","analog to digital","adc","a/d converter"]),
        ("Logic families (TTL/ECL/MOS/CMOS)",   ["ttl","ecl logic","cmos","mos logic","logic family"]),
      ],
    },
  },
  "Computer_Organization": {
    "book1": "Computer_Organization_book1.json",
    "book2": "Computer_Organization_book2.json",
    "units": {
      "Unit 1 - Basic organization": [
        ("Stored program & instruction cycle",  ["stored program","fetch","decode","execute","instruction cycle"]),
        ("Registers, operands, instruction format", ["instruction format","register","operand","opcode"]),
        ("Instruction sets & addressing modes", ["addressing mode","instruction set","immediate addressing","indirect addressing"]),
        ("Role of OS & compiler/assembler",     ["operating system","compiler","assembler"]),
      ],
      "Unit 2 - Arithmetic": [
        ("Number representation (fixed/floating)", ["fixed point","floating point","ieee 754","normalization"]),
        ("Adders (ripple/carry look-ahead)",    ["ripple","carry look-ahead","lookahead","carry generate","fast adder","binary adder","carry propagation"]),
        ("ALU design",                          ["arithmetic logic unit","alu design","alu"]),
        ("Booth's multiplication",              ["booth","booth's algorithm","booth multiplication"]),
        ("Division (restoring/non-restoring)",  ["restoring division","non-restoring","restoring algorithm"]),
      ],
      "Unit 3 - Memory": [
        ("CPU-memory interfacing",              ["memory interface","cpu-memory","memory interfacing","memory access","memory read","memory write"]),
        ("Memory organization (static/dynamic)", ["static memory","dynamic memory","sram","dram","memory organization"]),
        ("Memory hierarchy & associative memory", ["memory hierarchy","associative memory"]),
        ("Cache memory",                        ["cache memory","cache mapping","direct mapping","set associative"]),
        ("Virtual memory",                      ["virtual memory","paging","page replacement","address translation"]),
      ],
      "Unit 4 - Control & I/O": [
        ("Control unit (hardwired/microprogrammed)", ["hardwired control","microprogrammed","control unit","microinstruction"]),
        ("Instruction pipelining",              ["pipelining","pipeline hazard","instruction pipeline"]),
        ("RISC vs CISC",                        ["risc","cisc","reduced instruction set"]),
        ("I/O (handshaking/polled/interrupt/DMA)", ["handshaking","polled i/o","interrupt","direct memory access","dma"]),
      ],
    },
  },
  "Mathematics-III": {
    "book1": "Mathematics-III_book1.json",
    "book2": "Mathematics-III_book2.json",
    "units": {
      "Unit 1 - Sequences & Series": [
        ("Convergence of sequence & series",    ["convergence","sequence","series","cauchy"]),
        ("Tests for convergence",               ["ratio test","root test","comparison test","d'alembert","convergence test"]),
        ("Power / Taylor series",               ["power series","taylor series","maclaurin"]),
      ],
      "Unit 2 - Partial derivatives": [
        ("Limit, continuity, partial derivatives", ["partial derivative","limit and continuity","continuity"]),
        ("Chain rule, Jacobian, implicit fn",   ["chain rule","jacobian","implicit function"]),
        ("Maxima/minima & saddle points",       ["maxima and minima","saddle point","stationary point"]),
        ("Gradient, curl, divergence",          ["gradient","divergence","curl"]),
      ],
      "Unit 3 - Multiple integrals": [
        ("Double & triple integrals",           ["double integral","triple integral","double integration"]),
        ("Change of order / variables",         ["change of order","change of variable","polar coordinates"]),
        ("Green, Gauss, Stokes theorems",       ["green's theorem","gauss","stokes","divergence theorem"]),
      ],
      "Unit 4 - Differential equations": [
        ("First order ODE (exact/linear/Bernoulli)", ["exact differential","linear differential equation","bernoulli"]),
        ("Equations solvable for p/x/y, Clairaut", ["clairaut","solvable for p","singular solution"]),
        ("Second order linear ODE, D-operator", ["second order","d-operator","variation of parameters","cauchy-euler","cauchy euler"]),
      ],
      "Unit 5 - Graph theory": [
        ("Graph basics (walk/path/circuit/Euler/Hamiltonian)", ["euler graph","hamiltonian","walk","path","circuit","digraph"]),
        ("Matrix representation (incidence/adjacency)", ["incidence matrix","adjacency matrix"]),
        ("Trees & spanning (Kruskal/Prim)",     ["spanning tree","kruskal","prim","binary tree"]),
      ],
    },
  },
  "Economics_for_Engineers": {
    "book1": "Economics_for_Engineers_book1.json",
    "book2": "Economics_for_Engineers_book2.json",
    "units": {
      "Unit 1 - Costs & Estimation": [
        ("Economic decision making",            ["decision making","economic decision"]),
        ("Engineering costs (fixed/variable/marginal/sunk/opportunity)", ["fixed cost","variable cost","marginal cost","sunk cost","opportunity cost"]),
        ("Estimation models & learning curve",  ["cost estimation","per-unit model","segmenting model","power-sizing","learning curve"]),
      ],
      "Unit 2 - Cash flow & Rate of return": [
        ("Cash flow & time value of money",     ["cash flow","time value of money","interest formula"]),
        ("Nominal & effective interest",        ["nominal interest","effective interest"]),
        ("Rate of return & IRR",                ["rate of return","internal rate of return","irr"]),
        ("Present/Future worth & B-C analysis", ["present worth","future worth","benefit-cost","benefit cost"]),
      ],
      "Unit 3 - Inflation & Uncertainty": [
        ("Inflation & price indices",           ["inflation","price index","consumer price index","commodity index"]),
        ("Uncertainty & decision trees",        ["uncertainty","expected value","decision tree","probability","risk"]),
      ],
      "Unit 4 - Depreciation, Replacement, Accounting": [
        ("Depreciation methods",                ["depreciation","straight-line","declining balance","capital allowance"]),
        ("Replacement analysis",                ["replacement analysis","minimum cost life","economic life"]),
        ("Accounting & financial ratios",       ["balance sheet","income statement","financial ratio","cost accounting"]),
      ],
    },
  },
}

def verdict(h):
    if h == 0: return "Missing"
    if h <= 2: return "Weak"
    if h <= 6: return "Partial"
    return "Strong"

def load_pages(fname):
    with open(os.path.join(JDIR, fname), encoding="utf-8") as f:
        data = json.load(f)
    # returns list of (page_number, lowercased_text)
    return [(p["page"], (p.get("text") or "").lower()) for p in data["pages"]]

def scan(pages, keys):
    hits = []
    for pno, txt in pages:
        if any(k in txt for k in keys):
            hits.append(pno)
    return hits

for subj, cfg in SYLLABUS.items():
    print(f"\n=== {subj} ===")
    b1 = load_pages(cfg["book1"])
    b2 = load_pages(cfg["book2"])
    out = {"subject": subj, "book1_file": cfg["book1"], "book2_file": cfg["book2"], "units": {}}
    for unit, topics in cfg["units"].items():
        out["units"][unit] = []
        for name, keys in topics:
            h1 = scan(b1, keys); h2 = scan(b2, keys)
            rec = {
                "topic": name,
                "keys": keys,
                "book1": {"hits": len(h1), "pages": h1[:40], "verdict": verdict(len(h1))},
                "book2": {"hits": len(h2), "pages": h2[:40], "verdict": verdict(len(h2))},
                "best_source": "book1" if len(h1) >= len(h2) else "book2",
            }
            out["units"][unit].append(rec)
            print(f"  [{verdict(len(h1))[:4]:4}/{verdict(len(h2))[:4]:4}] b1={len(h1):3} b2={len(h2):3}  {name}")
    with open(os.path.join(OUT, f"{subj}_topicmap.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

print(f"\nDone. Topic maps -> {OUT}")
