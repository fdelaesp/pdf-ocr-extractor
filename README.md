# 📄 PDF OCR Extractor

This is a Python tool that extracts text from images inside PDF documents using **Tesseract OCR** and **Poppler**.

## 🔧 Requirements

- [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## ✅ Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/pdf-ocr-extractor.git
cd pdf-ocr-extractor
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Update paths** in `src/pdf_ocr.py`:
   - Set your `POPLER_PATH`
   - Set your `tesseract_cmd`

```python
POPLER_PATH = r"C:\Users\franc\Desktop\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## 🧠 Usage

Run the script from the terminal:

```bash
python src/pdf_ocr.py
```

You'll be prompted to enter the path of a PDF file. The tool will convert each page to an image and extract text using Tesseract.

## 🖼️ Sample Output

```
Enter the path to the PDF file: sample_pdfs/test.pdf

--- Page 1 ---
This is the extracted text from page 1...

--- Page 2 ---
This is the extracted text from page 2...
```

## 📂 Folder Structure

- `src/`: Core Python script
- `sample_pdfs/`: PDFs to test
- `requirements.txt`: Dependency list

---

## 👨‍💻 Author

Francisco de La Espriella – [GitHub](https://github.com/fdelaesp)

---

## 📜 License

This project is licensed under the MIT License.
