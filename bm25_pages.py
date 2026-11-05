import json
import re
from pathlib import Path
from rank_bm25 import BM25Okapi

project_folder = Path(__file__).resolve().parent
json_path = project_folder / "data" / "processed" / "visa_2025_pages.json"

with json_path.open("r", encoding="utf-8") as file:
    pages = json.load(file)

print("Page records loaded:", len(pages))

# we gonna turn each pages text into a list of words

stop_words = {"how", "much", "did", "in", "s", "the", "a", "an", "what", "was"}

tokenized_pages = []
for page_record in pages:
    words = re.findall(r"\b\w+\b", page_record["text"].lower())
    filtered_words = [] #empty list for words we wanna keep
    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    tokenized_pages.append(filtered_words)

print("Pages prepared:", len(tokenized_pages))
print("First page words:", tokenized_pages[0])

bm25 = BM25Okapi(tokenized_pages)
print("BM25 index ready.")

#bm is ready lets give bm25 a question and ask to score every page
query = input("Enter a question: ").strip()
query_words = re.findall(r"\b\w+\b", query.lower())

filtered_query = []
for word in query_words:
    if word not in stop_words:
        filtered_query.append(word)

if not filtered_query:
    print("Please enter a question with searchable words.")
else:
    scores = bm25.get_scores(filtered_query) #new one its to calulate a score for every page

    print("Question words:", filtered_query)
    print("Number of page scores:", len(scores))
    print("Score for PDF page 75:", scores[74])

    results = []

    for page_record, score in zip(pages, scores):
        results.append({
            "pdf_page": page_record["pdf_page"],
            "score": float(score),
        })

    results.sort(
        key=lambda result: (-result["score"], result["pdf_page"])
    )

    # we now try to find the rank of our verified evidence page, cause it missed thetop 5
    for rank, result in enumerate(results, start=1):
        if result["pdf_page"] == 75:
            print("Verified PDF page 75 ranked:", rank)
            break


    print("\nTop 5 BM25 pages:")

    for result in results[:5]:
        print(
            "PDF page:", result["pdf_page"],
            "| Score:", round(result["score"], 3)
        )
    #display the text of the five highest-ranked pahges.
    for result in results[:5]:
        pdf_page = result["pdf_page"]
        page_record = pages[pdf_page - 1]

        print("\n--- PDF page:", pdf_page, "---")
        print(page_record["text"])
