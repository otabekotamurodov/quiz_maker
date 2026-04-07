import os
import pdfplumber
from docx import Document

def parse_file(file_path: str) -> str:
    """
    File path qabul qiladi va ichidagi TEXT ni qaytaradi
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return _parse_pdf(file_path)

    elif ext == ".docx":
        return _parse_docx(file_path)

    elif ext == ".txt":
        return _parse_txt(file_path)

    else:
        raise ValueError("Unsupported file format")


def _parse_pdf(file_path: str) -> str:
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)


def _parse_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())


def _parse_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
