import os
import pickle
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

st.set_page_config(page_title="News Research Tool", layout="wide")
st.title("📰 News Research Tool")

VECTOR_DB_PATH = "faiss_store.pkl"

# Initialize session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar: URL Input ----------------
st.sidebar.header("Enter News URLs")
urls = st.sidebar.text_area(
    "One URL per line",
    height=180
).splitlines()

process_btn = st.sidebar.button("Process URLs")

# --------- PROCESS URLs ---------
if process_btn:
    if not urls or urls == [""]:
        st.error("❌ Please enter at least one valid URL.")
    else:
        st.info("📥 Loading articles...")
        loader = UnstructuredURLLoader(urls=urls)
        documents = loader.load()

        st.info("✂️ Splitting text...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=50
        )
        docs = text_splitter.split_documents(documents)

        # Limit chunks (safe + fast)
        docs = docs[:25]

        st.info("🧠 Creating FREE local embeddings...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = FAISS.from_documents(docs, embeddings)

        with open(VECTOR_DB_PATH, "wb") as f:
            pickle.dump(vectorstore, f)

        st.success("✅ Articles processed successfully!")

# --------- CHAT-STYLE Q&A ---------
if os.path.exists(VECTOR_DB_PATH):
    st.header("💬 Ask Questions from News")

    query = st.text_input("Type your question and hit Enter", key="input")

    if query:
        # Load vectorstore
        with open(VECTOR_DB_PATH, "rb") as f:
            vectorstore = pickle.load(f)

        # Retrieve relevant documents
        relevant_docs = vectorstore.similarity_search(query, k=4)
        context = "\n\n".join(doc.page_content for doc in relevant_docs)

        # Prepare prompt
        prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{query}
"""

        # Generate LLM response
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.2
        )
        response = llm.invoke(prompt)

        # Save conversation to session state
        st.session_state.messages.append({"user": query, "bot": response.content})

    # Display chat messages
    for msg in st.session_state.messages:
        st.chat_message("user").write(msg["user"])
        st.chat_message("assistant").write(msg["bot"])

    # Clear chat button (works without experimental_rerun)
    if st.button("Clear Chat"):
        st.session_state.messages = []
