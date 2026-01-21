import streamlit as st
from bd import funcoes
from utils.styles import inject_mobile_css

inject_mobile_css()

st.header('📝 Chamada', text_alignment= "left")

funcoes.tabturmas()