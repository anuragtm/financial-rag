import json
import re
from pathlib import Path
from transformers import AutoTokenizer

project_folder = Path(__file__).resolve().parent
json_path = project_folder / "data" / "processed" / "visa_2025_pages.json"

with json_path.open("r", encoding="utf-8") as file:
    pages = json.load(file)

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-small-en-v1.5")

prepared_pages = []

for page in pages:
    clean_text = re.sub(r"\.{3,}", " ", page["text"])
    tokens = tokenizer.tokenize(clean_text)

    prepared_pages.append({
        "source_file": page["source_file"],
        "pdf_page": page["pdf_page"],
        "text": clean_text,
        "token_count": len(tokens),
    })

print("Pages prepared:", len(prepared_pages))
print("PDF page 75 token count:", prepared_pages[74]["token_count"])