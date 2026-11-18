from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5", device = "cpu")
text = "Visa's net income was $20,058 million in 2025."

embedding = model.encode(text, normalize_embeddings=True)
print("Original text:", text)
print("Embedding shape:", embedding.shape)
print("First 5 numbers:", embedding[:5])