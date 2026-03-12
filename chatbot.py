import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

import json

from langchain_google_genai import GoogleGenerativeAIEmbeddings

api_key = st.secrets.get("GEMINI_API_KEY")
model = ChatGoogleGenerativeAI(
            model = 'gemini-2.5-flash',
            temperature = 0,
            max_tokens = None,
            google_api_key=api_key
        )
if api_key == None:
    st.error("Gemini api key not found. please add it in steamlit secrets")
    st.stop()

def load_data():
    docs = []
    loader = TextLoader("store_data/aboutus.md")
    docs += loader.load()
    with open("store_data/products.json", "r") as f:
        data = json.load(f)
        for item in data["products"]:
            content = f"{item['name']}: {item['description']} - Price: {item['price']}"
            docs.append(Document(page_content=content))
    return docs
def build_vectorstore():
    docs = load_data()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",google_api_key=api_key)
    return  FAISS.from_documents(splits, embeddings)

def ask_echo_heaven(question, api_key):

    db = build_vectorstore(api_key)

    retriever = db.as_retriever(search_kwargs={"k": 2})

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        google_api_key=api_key
    )

    prompt = f"""
    You are a helpful assistant for a store called Echo Heaven you can list products and prices of those products when asked.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.invoke(prompt)

    return response.content