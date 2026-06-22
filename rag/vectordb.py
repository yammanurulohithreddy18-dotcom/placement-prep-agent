import os
import chromadb

client = chromadb.HttpClient(
    host=os.getenv("CHROMA_HOST", "localhost"),
    port=int(os.getenv("CHROMA_PORT", "8000"))
)

collection = client.get_or_create_collection(
    name="companies"
)