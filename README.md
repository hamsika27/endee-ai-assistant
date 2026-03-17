# 🤖 Endee AI Knowledge Assistant

An intelligent documentation assistant built using the **Endee Vector Database**.
This project demonstrates how modern AI systems retrieve knowledge using **vector embeddings and semantic search**.

Instead of relying only on keyword matching, the system understands the **meaning of questions** and retrieves the most relevant information from documentation.

---

## 🚀 Project Overview

Modern AI applications rely on fast retrieval of relevant knowledge from large datasets.
This project implements a **semantic search chatbot** that allows users to ask questions about Endee and receive contextual answers.

The system works by converting text into numerical embeddings and storing them in a vector database. When a user asks a question, the system searches for the most similar embeddings and retrieves the relevant documentation.

---

## 🧠 Key AI Concept

### Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation combines **information retrieval with AI responses**.

Workflow:

User Question
↓
Convert question into embedding
↓
Search vector database for similar information
↓
Retrieve relevant documentation
↓
Display answer in chatbot interface

This approach ensures answers come from **real documentation rather than memorized information**.

---

## 🛠 Technologies Used

* **Endee Vector Database**
* **Sentence Transformers**
* **Python**
* **Streamlit**
* **NumPy**

---

## ⚙️ System Architecture

User Query
↓
Text Embedding (Sentence Transformer)
↓
Vector Similarity Search (Endee)
↓
Retrieve Relevant Documents
↓
Display Answer in Chat Interface

---

## ✨ Features

✔ Semantic document search
✔ Vector similarity retrieval
✔ AI documentation assistant
✔ Lightweight architecture
✔ Interactive chatbot interface
✔ Easy local deployment

---

## 📦 Project Structure

```
endee-ai-assistant
│
├── app.py
├── embed.py
├── vector_store.py
├── requirements.txt
│
├── data
│   └── endee_docs.txt
│
└── endee_db
```

---

## ⚡ Installation Guide

### Clone the repository

```
git clone https://github.com/hamsika27/endee-ai-assistant.git
cd endee-ai-assistant
```

### Install dependencies

```
pip install -r requirements.txt
```

### Generate embeddings

```
python embed.py
```

### Run the application

```
streamlit run app.py
```

The chatbot will open in your browser.

---

## 💬 Example Questions

Try asking the assistant:

• What is Endee?
• What is Retrieval-Augmented Generation?
• What are the features of Endee?
• How does semantic search work?

---

## 🎯 Practical Applications

* AI documentation assistants
* Knowledge base search systems
* Semantic search engines
* Intelligent customer support bots
* AI research tools

---

## 🌟 Why This Project Matters

Traditional search relies on **exact keywords**.

Vector databases enable systems to search based on **meaning and context**, which is essential for modern AI applications such as:

• RAG pipelines
• AI copilots
• Conversational assistants
• Recommendation systems

---

## 👩‍💻 Author

Hamsika
Aspiring Data Analyst | AI Enthusiast

---

## 📜 License

This project is created for educational purposes as part of the Tap Academy AI project evaluation.
