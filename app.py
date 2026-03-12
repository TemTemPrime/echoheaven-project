import streamlit as st
from chatbot import ask_echo_heaven

st.set_page_config(page_title= "EchoHaven Chatbot", page_icon="🌿")
st.title("🌿 EchoHaven Mart Chatbot")
st.write("Ask me anything about EcoHaven Mart!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history= []
query = st.text_input("Your question:", "")
if query:
    response = ask_echo_heaven(query)
    st.session_state.chat_history.append(("You", query))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in reversed(st.session_state.chat_history):
    st.write(f"**{sender}:** {message}")