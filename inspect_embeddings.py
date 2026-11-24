from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5", device = "cpu")
text = "Visa's net income was $20,058 million in 2025."

embedding = model.encode(text, normalize_embeddings=True)
print("Original text:", text)
print("Embedding shape:", embedding.shape)
print("First 5 numbers:", embedding[:5])

texts = [
    "Visa's net income was $20,058 million in 2025.",
    "Visa's net revenue was $40,000 million in 2025.",
]

embeddings = model.encode(texts, normalize_embeddings=True)

print("Number of texts:", len(texts))
print("Embeddings shape:", embeddings.shape)

for text, vector in zip(texts, embeddings):
    print("\nText:", text)
    print("Vector length:", len(vector))
    print("First 3 values:", vector[:3])

similarity = embeddings[0] @ embeddings[1]

print("\nSimilarity score:", float(similarity))

for index, vector in enumerate(embeddings, start=1):
    vector_length = (vector @ vector) ** 0.5
    print(f"Embedding {index} normalized length:", float(vector_length))