import streamlit as st
import pandas as pd
from bd.database import database_segment
from utils.styles import inject_mobile_css

inject_mobile_css()

st.set_page_config(
    page_icon= 'logo_ipb.png',
    page_title= 'EBD IPSO'
)

st.header('Escola Bíblica Dominical IPSO', text_alignment= "center") #write

database_segment()