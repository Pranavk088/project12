from typing import Union
from PyPDF2 import PdfReader
import os

def read_text_from_file(file_path: Union[str, bytes]) -> str:
    if isinstance(file_path, str):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".pdf":
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                return "\n".join([page.extract_text() or "" for page in reader.pages])
        elif ext == ".txt":
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            raise ValueError("Unsupported file type.")
    else:
        raise ValueError("Expected file path as string.")


