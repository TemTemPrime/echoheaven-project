import os
import streamlit as st
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import getpass
from dotenv import load_dotenv
import tempfile
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

api_key = st.secrets.get("GEMINI_API_KEY")