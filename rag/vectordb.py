import chromadb

client = chromadb.PersistentClient(path="memory/chroma_db")

collection = client.get_or_create_collection(
    name="companies"
)