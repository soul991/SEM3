#!/usr/bin/env python3
"""Build the StudyBooks PDFs with the colored template. Usage:
   python3 build_books.py <index...>   (0-9, see BOOKS list)"""
import subprocess, tempfile, os, re, sys

BOOKS = [
 ("Analog_and_Digital_Electronics/ADE_Concept_Book.md","21,101,192","ADE · ESC-301 · Concept Book"),
 ("Analog_and_Digital_Electronics/ADE_QA_Book.md","21,101,192","ADE · ESC-301 · Q\\&A Book"),
 ("Computer_Organization/CO_Concept_Book.md","0,105,92","Computer Organization · Concept Book"),
 ("Computer_Organization/CO_QA_Book.md","0,105,92","Computer Organization · Q\\&A Book"),
 ("Mathematics-III/M3_Concept_Book.md","94,53,177","Mathematics-III · Concept Book"),
 ("Mathematics-III/M3_QA_Book.md","94,53,177","Mathematics-III · Q\\&A Book"),
 ("Economics_for_Engineers/ECO_Concept_Book.md","183,88,0","Economics · Concept Book"),
 ("Economics_for_Engineers/ECO_QA_Book.md","183,88,0","Economics · Q\\&A Book"),
 ("README.md","31,97,141","Sem-3 StudyBooks · Index"),
 ("DSA/DSA_Video_Guide.md","84,84,110","DSA · Video Guide"),
]

def build(md, rgb, short):
    txt = open(md, encoding="utf-8").read()
    for k,v in {"📺":"► ","📚":"","⟹":"⇒","∯":"∮","⋅":"·","🔥":"","✍":"","🎯":"","✅":"[OK]"}.items():
        txt = txt.replace(k,v)
    tmp = tempfile.NamedTemporaryFile("w",suffix=".md",delete=False,encoding="utf-8"); tmp.write(txt); tmp.close()
    d = tempfile.NamedTemporaryFile("w",suffix=".tex",delete=False,encoding="utf-8")
    d.write("\\def\\accentRGB{%s}\n\\def\\booktitleshort{%s}\n" % (rgb, short)); d.close()
    out = md[:-3]+".pdf"
    title = os.path.basename(md)[:-3].replace("_"," ")
    r = subprocess.run(["pandoc",tmp.name,"-o",out,"--pdf-engine=xelatex",
        "--include-in-header",d.name,"--include-in-header","book_style.tex",
        "-V","mainfont=DejaVu Sans","-V","monofont=DejaVu Sans Mono",
        "-V","geometry:margin=2cm","-V","fontsize=10pt","-V","linestretch=1.06",
        "--metadata",f"title={title}","--toc","--toc-depth=2"],
        capture_output=True,text=True,timeout=560)
    ok = os.path.exists(out) and r.returncode==0
    warn = len(re.findall("Missing character", r.stderr))
    size = os.path.getsize(out)//1024 if os.path.exists(out) else 0
    print(("OK  " if ok else "FAIL ")+f"{out} ({size} KB, {warn} glyph warnings)")
    if not ok: print(r.stderr[-1200:])
    os.unlink(tmp.name); os.unlink(d.name)
    return ok

if __name__ == "__main__":
    idxs = [int(a) for a in sys.argv[1:]] or range(len(BOOKS))
    for i in idxs: build(*BOOKS[i])
