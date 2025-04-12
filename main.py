from pdf2image import convert_from_path
import pytesseract

# Static path for Poppler (already set)
POPLER_PATH = r"C:\Users\franc\Desktop\poppler-24.08.0\Library\bin"

# Set the Tesseract executable path (this must point to tesseract.exe)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def pdf_to_text(pdf_path, dpi=300):
    """
    Extracts text from images in each page of a PDF document.

    Args:
        pdf_path (str): The path to the PDF document.
        dpi (int): The resolution used for converting PDF pages to images.

    Returns:
        str: The extracted text from the PDF document.
    """
    try:
        pages = convert_from_path(pdf_path, dpi=dpi, poppler_path=POPLER_PATH)
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return ""

    all_text = ""
    for i, page in enumerate(pages):
        try:
            text = pytesseract.image_to_string(page)
            all_text += f"\n--- Page {i + 1} ---\n{text}"
        except Exception as e:
            print(f"Error processing page {i + 1} for OCR: {e}")

    return all_text


def main():
    pdf_file = input("Enter the path to the PDF file: ").strip()
    text = pdf_to_text(pdf_file)

    print("\nExtracted Text:\n")
    print(text)


if __name__ == "__main__":
    main()
