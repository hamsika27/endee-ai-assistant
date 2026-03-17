from sentence_transformers import SentenceTransformer
from vector_store import EndeeVectorStore
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("data/endee_docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 10]

vector_store = EndeeVectorStore(dim=384)

embeddings = model.encode(chunks)

for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
    vector_store.add(
        id=i,
        embedding=emb.tolist(),
        metadata={"text": chunk}
    )

os.makedirs("endee_db", exist_ok=True)
vector_store.save("endee_db")

print(f"✅ Successfully embedded {len(chunks)} chunks and saved to endee_db/")