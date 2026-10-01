import numpy as np
import chromadb

# comparing using cosine similarity
def cosine_similarity(vec1,vec2): 
    return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
#output ranges from -1 to 1 if:
# 1= very similar
# 0= unrelated
# -1 =opposite

client=chromadb.PersistentClient()
collection = client.get_collection("vehicles_embeddings")

data=collection.get(include=["documents","embeddings"])

# Get embeddings
emb_car = data["embeddings"][0]
emb_bus = data["embeddings"][1]
emb_cycle = data["embeddings"] [2]

#compare similarity
sim_car_bus=cosine_similarity(emb_car,emb_bus)
sim_bus_cycle=cosine_similarity(emb_bus,emb_cycle)

print("cosine similarity between car and bus:" ,sim_car_bus)
print("cosine similarity between bus and cycle: ",sim_bus_cycle)

