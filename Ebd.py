import streamlit as st
import pandas as pd
from bd import funcoes
from bd.database import database_segment

st.set_page_config(
    page_icon= 'logo_ipb.png',
    page_title= 'EBD IPSO',
    primaryColor = '#4CAf50'
)

st.header('Escola Bíblica Dominical IPSO', text_alignment= "center") #write


database_segment()

