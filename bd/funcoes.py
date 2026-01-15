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
            df = supabase.table('alunos').select('nome').filter('classe','eq',turma).execute()
            return df.data
        with tab:
            res = listardados(turma)
            st.write('Turmas:')             #header
            df = pd.DataFrame(res)          #criando df
            df['presenca'] = False         #criando coluna de presença com todos pendente de presença
            
            # Flag para bloquear o botão após salvar
            saved_key = f"salvo_{turma}"
            if saved_key not in st.session_state:
                st.session_state[saved_key] = False

            #Tabela editavel antes de salvar            
            edited_df = st.data_editor(df, disabled=["nome"], key=f"editor_{turma}") 
            
            # Botão salvar 
            if st.button('Salvar', key=f"salvar_{turma}", disabled=st.session_state[saved_key]): 
                st.session_state[saved_key] = True  # bloqueia o botão
                st.write("Dados salvos:")
                st.data_editor(edited_df,disabled=["nome", "presenca"], key=f"final_{turma}")        # bloqueia tudo na tabela final

            Exemplo: enviar para supabase
            # supabase.table('alunos').upsert(edited_df.to_dict(orient="records")).execute()

            # Se já salvou, mantém a tabela final visível
            if st.session_state[saved_key]:
                st.write("Dados salvos:")
                st.data_editor(edited_df,disabled=["nome", "presenca"],key=f"final_{turma}")
