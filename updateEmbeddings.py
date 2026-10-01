import numpy as np
import chromadb

# 1: Connect to chroma persistent storage
client= chromadb.PersistentClient()

# 2: Get the data
collection= client.get_collection(name="vehicles_embeddings")

#update
collection.update(
    ids=["bus1"],
    documents=["bus runs on electricity instead of petrol"]
)

print("Document updated")