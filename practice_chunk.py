import json
from pathlib import Path


project_folder = Path(__file__).resolve().parent
json_path = project_folder / "data" / "processed" / "visa_2025_pages.json"

with json_path.open("r", encoding="utf-8") as file: #let our JSON file for reading
    pages = json.load(file)
page = pages[74]
chunk_lines =[]

for line in page["text"].splitlines():
    if line.startswith(("2025 2024 2023", "(in millions", "Net income ")):
        chunk_lines.append(line)

chunk = {"source_file": page["source_file"],
    "pdf_page": page["pdf_page"],
    "text": "\n".join(chunk_lines),

}
print(chunk)

output_path = json_path.parent / "visa_practice_chunk.json"
with output_path.open("w", encoding="utf-8") as file:
    json.dump(chunk, file, indent=2)

print("Chunk saved to:", output_path)