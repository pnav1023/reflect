import streamlit as st
from rag_scripts import get_top_n_similar
from llm_req import get_chat_bot

st.title('Reflect AI')

get_chat_bot(get_top_n_similar("Places I've been"))