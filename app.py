import streamlit as st

st.set_page_config(page_title= "EchoHaven Chatbot", page_icon="🌿")
st.title("🌿 EchoHaven Mart Chatbot")
st.write("Ask me anything about EcoHaven Mart!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history= []