import chromadb

# 1: Connect to chroma persistent storage
client= chromadb.PersistentClient()

# 2: Get the data
collection= client.get_collection(name="vehicles_embeddings")

# 3: Retrieve embeddings from each document
data=collection.get(include=["documents","embeddings"])

for id,text,emb in zip(data["ids"],data["documents"],data["embeddings"]):
    print(f"\n {id}: {text}")
    print(f"Embedding (first 10 value): {emb[:10]}")