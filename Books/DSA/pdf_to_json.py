import os
import json
import fitz  # PyMuPDF
import pytesseract
from PIL import Image


# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

# If Windows cannot find tesseract automatically, uncomment
# the next line and change the path if necessary.
#
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )

OCR_LANGUAGE = "eng"

# If a page contains less text than this, OCR will be used.
MIN_TEXT_LENGTH = 30


# ---------------------------------------------------------
# EXTRACT TEXT FROM A PDF PAGE
# ---------------------------------------------------------

def extract_page_text(page):
    """
    First try normal PDF text extraction.
    If the PDF is scanned/image-based, use OCR.
    """

    text = page.get_text("text").strip()

    # Normal text extraction worked
    if len(text) >= MIN_TEXT_LENGTH:
        return text

    # -----------------------------------------------------
    # OCR FALLBACK
    # -----------------------------------------------------

    print("    Using OCR...")

    # Render PDF page as an image.
    # 2x resolution gives Tesseract better results.
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)

    image = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    text = pytesseract.image_to_string(
        image,
        lang=OCR_LANGUAGE
    )

    return text.strip()


# ---------------------------------------------------------
# PROCESS ONE PDF
# ---------------------------------------------------------

def process_pdf(pdf_path):

    filename = os.path.basename(pdf_path)
    book_name = os.path.splitext(filename)[0]

    print("\n" + "=" * 60)
    print(f"Processing: {filename}")
    print("=" * 60)

    doc = fitz.open(pdf_path)

    pages = []

    total_pages = len(doc)

    for page_number, page in enumerate(doc, start=1):

        print(f"Page {page_number}/{total_pages}")

        text = extract_page_text(page)

        pages.append({
            "page": page_number,
            "text": text
        })

    # -----------------------------------------------------
    # CREATE JSON
    # -----------------------------------------------------

    output = {
        "book": book_name,
        "source_file": filename,
        "page_count": total_pages,
        "pages": pages
    }

    # Same folder as the PDF
    output_path = os.path.join(
        os.path.dirname(pdf_path),
        book_name + ".json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(f"\nSaved: {output_path}")


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    # Folder where this Python script is located
    folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    # Find PDFs in the same folder
    pdf_files = [
        os.path.join(folder, file)
        for file in os.listdir(folder)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("No PDF files found in this folder.")
        return

    print(f"Found {len(pdf_files)} PDF file(s).")

    for pdf_path in pdf_files:

        try:
            process_pdf(pdf_path)

        except Exception as e:

            print(f"\nERROR processing:")
            print(f"  {pdf_path}")
            print(f"  {e}")

    print("\n" + "=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    main()