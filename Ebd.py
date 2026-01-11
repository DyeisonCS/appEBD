import streamlit as st
import pandas as pd
from bd import funcoes
from supabase import create_client, Client
from bd.database import database_segment

#url = os.environ["SUPABASE_URL"]
#key = os.environ["SUPABASE_KEY"]
#supabase = create_client(url, key)

#url = "https://vncdlatpuvniwwzdebtb.supabase.co"
#key = "sb_publishable_X5t9KZPR-0LJZF0BaMRT5w_rmhCUW6h"
#supabase: Client = create_client(url, key)


st.set_page_config(
    page_icon= 'logo_ipb.png',
    page_title= 'EBD IPSO'
)

st.header('Escola Bíblica Dominical IPSO', text_alignment= "center") #write

database_segment()