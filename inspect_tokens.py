import json
import re

from pathlib import Path


from transformers import AutoTokenizer

load_tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-small-en-v1.5")

text = "Visa's net income was $20,058 million in 2025."

tokens = load_tokenizer.tokenize(text) #splits our sentence into text and save resulting pieces in tokens.

print("Original text: ", text)
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))

project_folder = Path(__file__).resolve().parent
chunk_path = project_folder / "data" / "processed" / "visa_practice_chunk.json"

with chunk_path.open("r", encoding="utf-8") as file:
    chunk = json.load(file)

chunk_tokens = load_tokenizer.tokenize(chunk["text"])
print("\n Chunk text:", chunk["text"])
print("Chunk token count:", len(chunk_tokens))


clean_text = re.sub(r"\.{3}", " ", chunk["text"])
clean_tokens = load_tokenizer.tokenize(clean_text)

print("\nCleaned chunk:", clean_text)
print("Tokens before cleaning:", len(chunk_tokens))
print("Tokens after cleaning:", len(clean_tokens))