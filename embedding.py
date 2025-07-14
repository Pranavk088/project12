from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def split_into_chunks(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def create_faiss_index(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    return index, chunks

def search_index(query, index, chunks, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [chunks[i] for i in I[0]]
