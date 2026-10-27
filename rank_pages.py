import json
import pathlib from Path

import re
# re for findin text patterns

query = input("Enter a question: ").strip()

query_words = set(re.findall(r"\b\w+\b", query.lower()))

print("Unique query words:", sorted(query_words)) #sorted() to displays the words alphabetically for ease inspection



stop_words = {"how", "much", "did", "in", "s", "the", "a", "an"}

search_words = query_words - stop_words

print("Words used for ranking:", sorted(search_words))