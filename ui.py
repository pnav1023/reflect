import streamlit as st
from rag_scripts import get_top_n_similar
from llm_req import get_question

st.title('Reflect AI')

st.code(get_question(get_top_n_similar("Places I've been")))