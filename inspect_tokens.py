from transformers import AutoTokenizer

load_tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-small-en-v1.5")

text = "Visa's net income was $20,058 million in 2025."

tokens = load_tokenizer.tokenize(text) #splits our sentence into text and save resulting pieces in tokens.

print("Original text: ", text)
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))