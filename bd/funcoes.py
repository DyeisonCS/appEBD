import streamlit as st
from supabase import create_client, Client
import pandas as pd
import os

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

turmas = supabase.table('alunos').select('classe').execute()

df = pd.DataFrame(turmas.data)
lista_unica = list(df['classe'].unique())


def tabturmas():
    tabs = st.tabs(lista_unica)
    for tab, turma in zip(tabs, lista_unica):
        def listardados(turma):
            df = supabase.table('alunos').select('classe').filter('classe','eq',turma).execute()
            return df.data
        with tab:
            res = listardados(turma)
            st.write('Turmas:')             #header
            df = pd.DataFrame(res)          #criando df
            df['presenca'] = False         #criando coluna de presença com todos pendente de presença
            st.data_editor(df) 
