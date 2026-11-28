## Now embed_chunks.py applies what we learned to our 304 actual report chunks, instead of handwritten example sentences in inspect_embed...

import json
from pathlib import Path

project_folder = Path(__file__).resolve().parent
chunks_path = project_folder / "data" / "processed" / "visa_2025_chunks.json"

with chunks_path.open("r", encoding="utf-8") as file:
    chunks = json.load(file)

texts = [chunk["text"] for chunk in chunks]
## texts means go through every chunk, take its text, and collect those texts into a list.

print("Chunks loaded:", len(chunks))
print("Texts ready for embedding:", len(texts))    