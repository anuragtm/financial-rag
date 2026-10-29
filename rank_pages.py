import json
from pathlib import Path

import re
# re for findin text patterns

query = input("Enter a question: ").strip()

query_words = set(re.findall(r"\b\w+\b", query.lower()))

print("Unique query words:", sorted(query_words)) #sorted() to displays the words alphabetically for ease inspection



stop_words = {"how", "much", "did", "in", "s", "the", "a", "an"}

search_words = query_words - stop_words

print("Words used for ranking:", sorted(search_words))

#now counting how many of those words appear on one page, before ranking all pages

project_folder  = Path(__file__).resolve().parent
json_path = project_folder / "data" / "processed" / "visa_2025_pages.json"

with json_path.open("r", encoding="utf-8") as file:
    pages = json.load(file)

# for temp inspect our verified evidence page
page_record = pages[74]

page_words = set(re.findall(r"\b\w+\b", page_record["text"].lower()))

matched_words = search_words & page_words
score = len(matched_words)

print("PDF page:", page_record["pdf_page"])
print("Matched words:", sorted(matched_words))
print("Score:", score)