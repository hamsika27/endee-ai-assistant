import sys
import os
import importlib.util
import streamlit as st
from sentence_transformers import SentenceTransformer

# --- 1. HARD IMPORT FIX ---
script_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(script_dir, "vector_store.py")

if not os.path.exists(module_path):
    st.error(f"CRITICAL ERROR: Could not find 'vector_store.py' at {module_path}")
    st.stop()

spec = importlib.util.spec_from_file_location("vector_store", module_path)
vector_store_module = importlib.util.module_from_spec(spec)
sys.modules["vector_store"] = vector_store_module
spec.loader.exec_module(vector_store_module)

from vector_store import EndeeVectorStore

# --- 2. LOAD MODEL AND VECTOR DATABASE ---
@st.cache_resource
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    db_path = os.path.join(script_dir, "endee_db")
    vector_store = EndeeVectorStore.load(db_path)
    return model, vector_store

model, vector_store = load_resources()

# --- 3. RETRIEVE RELEVANT DOCUMENTS ---
def retrieve_relevant_chunks(query, top_k=3):

    query_embedding = model.encode([query])
    results = vector_store.search(query_embedding[0], k=top_k)

    return [r.metadata["text"] for r in results]


# --- 4. GENERATE ANSWER ---
def generate_answer(query):

    chunks = retrieve_relevant_chunks(query)

    if not chunks:
        return "❌ I couldn't find an answer in the Endee documentation."

    formatted_answer = "📄 **Relevant Documentation:**\n\n"

    for i, chunk in enumerate(chunks, 1):
        formatted_answer += f"**{i}.** {chunk}\n\n"

    return formatted_answer


# --- 5. STREAMLIT UI ---
st.set_page_config(
    page_title="Endee AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Endee AI Assistant")
st.subheader("Ask me anything about Endee!")

query = st.text_input(
    "Type your question:",
    placeholder="Example: What is Endee?"
)

if query:

    with st.spinner("Searching documentation..."):

        answer = generate_answer(query)

    st.success("Answer Found")
    st.markdown(answer)


# --- 6. SIDEBAR ---
st.sidebar.title("About This Project")

st.sidebar.info("""
This AI assistant demonstrates semantic search using the Endee vector database.

Technologies used:

• Endee Vector Database  
• Sentence Transformers  
• Streamlit  

Use cases include:

• Retrieval-Augmented Generation (RAG)
• Semantic search
• AI documentation assistant

Project built for Tap Academy  
Assignment ID: TAP-JOB-ID-2458
""")