import json
from pathlib import Path
from pypdf import PdfReader

project_folder = Path(__file__).resolve().parent
pdf_path = project_folder / "data" / "raw" / "visa_2025_annual_report.pdf"

output_folder = project_folder / "data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)

reader = PdfReader(pdf_path)
pages = []

for page_number, page in enumerate(reader.pages, start = 1):
    page_record = {
        "source_file": pdf_path.name,
        "pdf_page": page_number,
        "text": page.extract_text() or "",
    }
    pages.append(page_record)
output_path = output_folder / "visa_2025_pages.json"

with output_path.open("w", encoding="utf-8") as file:  #Open the file at this location for writingg
    json.dump(pages, file, ensure_ascii=False, indent=2) #writes our Records

print("Pages saved:", len(pages))
print("Saved to:", output_path)