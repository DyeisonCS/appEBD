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
            

            
            # Inicializa estado
            if f"edited_df_{turma}" not in st.session_state:
                st.session_state[f"edited_df_{turma}"] = df.copy()
            if f"salvo_{turma}" not in st.session_state:
                st.session_state[f"salvo_{turma}"] = False
            
            # Define colunas bloqueadas
            disabled_cols = ["nome"]
            if st.session_state[f"salvo_{turma}"]:
                disabled_cols.append("presenca")
            
            # Editor com estado persistente
            edited_df = st.data_editor(
                st.session_state[f"edited_df_{turma}"],
                disabled=disabled_cols,
                key=f"editor_{turma}"
            )
            
            # Atualiza estado com edições
            st.session_state[f"edited_df_{turma}"] = edited_df
            
            # Botão salvar
            salvar = st.button('Salvar', key=f"salvar_{turma}")
            
            # Se clicou salvar, bloqueia edição
            if salvar:
                st.session_state[f"salvo_{turma}"] = True
                st.success("Presenças salvas com sucesso!")
                # Aqui você pode enviar para o banco:
                # supabase.table('alunos').upsert(edited_df.to_dict(orient="records")).execute()
