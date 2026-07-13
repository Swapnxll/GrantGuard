#pdf_loader.py
# PDF → raw text

import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from every page of a PDF.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        Complete text extracted from the PDF.
    """

    document = fitz.open(pdf_path)

    pages = []

    try:
        for page in document:
            pages.append(page.get_text("text"))

    finally:
        document.close()

    return "\n".join(pages).strip()