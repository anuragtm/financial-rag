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
    clean_text = re.sub(r"\.{3,}", " ", page["text"]) #cleanup line for dots
    tokens = tokenizer.tokenize(clean_text)

    prepared_pages.append({
        "source_file": page["source_file"],
        "pdf_page": page["pdf_page"],
        "text": clean_text,
        "token_count": len(tokens),})

print("Pages prepared:", len(prepared_pages))
print("PDF page 75 token count:", prepared_pages[74]["token_count"])


#next splitting pages into chunks

max_chunk_tokens = 400
chunks = []

for page in prepared_pages:
    current_lines = []

    for line in page["text"].splitlines():
        if not line.strip():
            continue

        line_token_count = len(tokenizer.tokenize(line))

        if line_token_count > max_chunk_tokens:
            raise ValueError(
                f"PDF page {page['pdf_page']} has a line with "
                f"{line_token_count} tokens. This line needs splitting."
            )

        candidate_text = "\n".join(current_lines + [line])
        candidate_count = len(tokenizer.tokenize(candidate_text))

        if candidate_count > max_chunk_tokens:
            chunk_text = "\n".join(current_lines)

            chunks.append({
                "chunk_id": len(chunks) + 1,
                "source_file": page["source_file"],
                "pdf_page": page["pdf_page"],
                "text": chunk_text,
                "token_count": len(tokenizer.tokenize(chunk_text)),
            })

            current_lines = [line]
        else:
            current_lines.append(line)

    # Save the last chunk remaining on this page.
    if current_lines:
        chunk_text = "\n".join(current_lines)

        chunks.append({
            "chunk_id": len(chunks) + 1,
            "source_file": page["source_file"],
            "pdf_page": page["pdf_page"],
            "text": chunk_text,
            "token_count": len(tokenizer.tokenize(chunk_text)),
        })

print("Chunks created:", len(chunks))

for chunk in chunks:
    if chunk["pdf_page"] == 75:
        print("\nChunk:", chunk["chunk_id"])
        print("Text tokens:", chunk["token_count"])
        print(chunk["text"])