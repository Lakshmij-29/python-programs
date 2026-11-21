from pathlib import Path
import fitz

folder = Path("documents")
for pdf_file in folder.glob("*.pdf"):
    document = fitz.open(pdf_file)
    text = "\n".join(page.get_text() for page in document)
    output = pdf_file.with_suffix(".txt")
    output.write_text(text, encoding="utf-8")
    print("Extracted:", output.name)
