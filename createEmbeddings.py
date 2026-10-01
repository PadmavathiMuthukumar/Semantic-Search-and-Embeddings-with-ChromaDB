import chromadb

# 1: Connect to chroma persistent storage
client= chromadb.PersistentClient()

# 2: Create or reuse a collection
collection= client.get_or_create_collection(name="vehicles_embeddings")

print("Collection is ready:",collection.name)

# 3:Add documents to the collection
collection.add(
    documents=[
"Bus carries passengers on road",
"Plane flies across countries",
"Boat travels on water",
"Bicycle runs without fuel"
],
    ids=["bus1", "plane1", "boat1", "cycle1"],

)

print("Documents added with embeddings automatically generated!!")
