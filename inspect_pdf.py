from pathlib import Path
from pypdf import PdfReader

project_folder = Path(__file__).resolve().parent
pdf_path = project_folder / "data" / "raw" / "visa_2025_annual_report.pdf"

reader = PdfReader(pdf_path)
print("File:", pdf_path.name)
print("Total pages:", len(reader.pages))
first_page = reader.pages[0]
text = first_page.extract_text() or ""

print("\n First page text preview:")
print(text[:1000])

#tryin to find pages mentioning net revenue

print("\nPages mentioning net revenue:")
for page_number, page in enumerate(reader.pages, start=1):
    page_text = page.extract_text() or ""

    if "net revenue" in page_text.lower():
        print("PDF page:", page_number)


print("\nCandidate pages containing both revenue values:")

for page_number, page in enumerate(reader.pages, start=1):
    page_text = page.extract_text() or "" #uses empty text if nothing is returned
    
    if(
        "net revenue" in page_text.lower()
        and "40,000" in page_text  # and for all three conditions must be True
        and "35,926" in page_text  # in checks whether the text contains that exact sequence of characters.
    ):
        print("\nPDF page:", page_number)
        print(page_text)