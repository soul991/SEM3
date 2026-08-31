#!/usr/bin/env python3
"""
extract_books_to_json.py
------------------------------------------------------------
Walks the `Books/` directory. Each sub-folder is a SUBJECT and
contains (up to) two source PDF books. For every book this script:

  1. Tries fast native text extraction (for digital/text PDFs).
  2. Falls back to OCR (Tesseract) for pages that are scanned images.
  3. Stores the full extracted text, page-by-page, into a JSON file
     named:  <SubjectName>_book1.json  /  <SubjectName>_book2.json

Output JSONs are written to an `extracted_json/` folder.

------------------------------------------------------------
SETUP (run once in a terminal):

  # System OCR engine + Poppler (macOS via Homebrew)
  brew install tesseract poppler

  # Python libraries
  pip install pymupdf pdf2image pytesseract pillow

(On Linux:  sudo apt install tesseract-ocr poppler-utils )
------------------------------------------------------------
USAGE:
  python3 extract_books_to_json.py
"""

import os
import re
import sys
import json
from datetime import datetime

# ---- Third-party libs (see SETUP above) ----------------------------------
try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Missing dependency 'pymupdf'. Run: pip install pymupdf")

try:
    import pytesseract
    from pdf2image import convert_from_path
    from PIL import Image  # noqa: F401  (used indirectly by pdf2image)
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False


# --------------------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------------------
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
BOOKS_DIR  = os.path.join(BASE_DIR, "Books")
OUTPUT_DIR = os.path.join(BASE_DIR, "extracted_json")

# If a page's native text has fewer characters than this, treat the page as
# a scanned image and run OCR on it instead.
MIN_CHARS_FOR_NATIVE = 40

# DPI used when rasterizing a page for OCR. Higher = better accuracy, slower.
OCR_DPI = 300


# --------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------
def sanitize(name: str) -> str:
    """Turn a subject folder name into a clean file-safe token.
    'Analog & Digital Electronics' -> 'Analog_Digital_Electronics'
    """
    name = name.replace("&", "and")
    name = re.sub(r"[^\w\s-]", "", name)   # drop punctuation
    name = re.sub(r"\s+", "_", name.strip())
    return name


def clean_text(text: str) -> str:
    """Light normalization: collapse excess blank lines / trailing spaces."""
    text = text.replace("\x00", "")
    lines = [ln.rstrip() for ln in text.splitlines()]
    # collapse 3+ blank lines into a single blank line
    out, blanks = [], 0
    for ln in lines:
        if ln.strip() == "":
            blanks += 1
            if blanks <= 1:
                out.append("")
        else:
            blanks = 0
            out.append(ln)
    return "\n".join(out).strip()


def ocr_page(pdf_path: str, page_number: int) -> str:
    """OCR a single page (1-indexed) of a PDF and return its text."""
    if not OCR_AVAILABLE:
        return ""
    try:
        images = convert_from_path(
            pdf_path,
            dpi=OCR_DPI,
            first_page=page_number,
            last_page=page_number,
        )
        if not images:
            return ""
        return pytesseract.image_to_string(images[0])
    except Exception as e:
        print(f"      ! OCR failed on page {page_number}: {e}")
        return ""


def extract_pdf(pdf_path: str) -> dict:
    """Extract text from every page, using OCR as a fallback."""
    doc = fitz.open(pdf_path)
    pages = []
    ocr_pages = 0

    print(f"    -> {len(doc)} pages")
    for i, page in enumerate(doc, start=1):
        native = page.get_text("text") or ""
        if len(native.strip()) >= MIN_CHARS_FOR_NATIVE:
            method = "native"
            text = native
        else:
            # Likely a scanned/image page -> OCR it
            text = ocr_page(pdf_path, i)
            method = "ocr"
            if text.strip():
                ocr_pages += 1

        pages.append({
            "page": i,
            "method": method,
            "text": clean_text(text),
        })

        if i % 25 == 0:
            print(f"       ...processed {i}/{len(doc)} pages")

    doc.close()

    full_text = "\n\n".join(p["text"] for p in pages if p["text"])
    return {
        "num_pages": len(pages),
        "ocr_pages": ocr_pages,
        "char_count": len(full_text),
        "pages": pages,
        "full_text": full_text,
    }


# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------
def main():
    if not os.path.isdir(BOOKS_DIR):
        sys.exit(f"Books directory not found: {BOOKS_DIR}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not OCR_AVAILABLE:
        print("WARNING: OCR libraries not installed. Scanned pages will be "
              "skipped.\n         Install with: pip install pdf2image "
              "pytesseract pillow  (and: brew install tesseract poppler)\n")

    subjects = sorted(
        d for d in os.listdir(BOOKS_DIR)
        if os.path.isdir(os.path.join(BOOKS_DIR, d))
    )

    if not subjects:
        sys.exit("No subject folders found inside Books/.")

    summary = []
    for subject in subjects:
        subject_dir = os.path.join(BOOKS_DIR, subject)
        pdfs = sorted(
            f for f in os.listdir(subject_dir)
            if f.lower().endswith(".pdf")
        )
        if not pdfs:
            print(f"[{subject}] no PDFs found, skipping.")
            continue

        subj_token = sanitize(subject)
        print(f"\n=== Subject: {subject}  ({len(pdfs)} book(s)) ===")

        for idx, pdf_name in enumerate(pdfs, start=1):
            pdf_path = os.path.join(subject_dir, pdf_name)
            out_name = f"{subj_token}_book{idx}.json"
            out_path = os.path.join(OUTPUT_DIR, out_name)

            print(f"  Book {idx}: {pdf_name}")
            try:
                data = extract_pdf(pdf_path)
            except Exception as e:
                print(f"    !! Failed to process: {e}")
                continue

            record = {
                "subject": subject,
                "book_number": idx,
                "book_label": f"book{idx}",
                "source_filename": pdf_name,
                "extracted_at": datetime.now().isoformat(timespec="seconds"),
                **data,
            }

            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(record, fh, ensure_ascii=False, indent=2)

            print(f"    saved -> {out_name}  "
                  f"({data['char_count']:,} chars, "
                  f"{data['ocr_pages']} OCR pages)")

            summary.append({
                "subject": subject,
                "book": f"book{idx}",
                "source": pdf_name,
                "json": out_name,
                "pages": data["num_pages"],
                "chars": data["char_count"],
            })

    # write a small index of everything produced
    with open(os.path.join(OUTPUT_DIR, "_index.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)

    print(f"\nDone. {len(summary)} JSON file(s) written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
