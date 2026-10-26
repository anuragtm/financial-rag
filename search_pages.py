# now loading Json back into python
import json
from pathlib import Path

project_folder = Path(__file__).resolve().parent
json_path = project_folder / "data" / "processed" / "visa_2025_pages.json"

with json_path.open("r", encoding="utf-8") as file:
    pages = json.load(file) #reads them back

print("Page records loaded: ", len(pages))


#tryin to search them using a phrase I type
# First retrieval baseline: search saved page text for an exact phrase.

query = input("Enter a search phraase: ").strip().lower()  #strip for removing spaces from beginnin and the end

if not query:
    print("Please entery a non-empty search phrase.")
else:
    matches = 0

    for page_record in pages:
        if query in page_record["text"].lower():
            print(
                "Source:", page_record["source_file"],
                "| PDF page:", page_record["pdf_page"]
            )
            matches +=1

    print("Matching pages:", matches)


