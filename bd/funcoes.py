import streamlit as st
from supabase import create_client, Client
import pandas as pd
import datetime
import os
from utils.styles import inject_mobile_css

inject_mobile_css()

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

turmas = supabase.table('alunos').select('classe').execute()

df = pd.DataFrame(turmas.data)
lista_unica = list(df['classe'].unique())


def tabturmas():
    tabs = st.tabs(lista_unica)
    for tab, turma in zip(tabs, lista_unica):
        def listaturma(turma):
            df = supabase.table('alunos').select('nome').filter('classe','eq',turma).execute()
            return df.data
        
                    
        with tab:
            res = listaturma(turma)         #header
            df = pd.DataFrame(res)          #criando df
            df['presenca'] = False          #criando coluna de presença com todos pendente de presença
            df['biblia'] = False
            df['revista'] = False
            #st.data_editor(df)

            salvar_key = f"salvar_{turma}" 
            editor_key = f"editor_{turma}"

            hoje = datetime.date.today().isoformat()
            df_presenca = supabase.table('fct_presenca').select(
                'nome','classe','presenca','biblia','revista','data'
                ).filter('data', 'eq', hoje).filter('classe','eq',turma).execute().data

            if salvar_key not in st.session_state:
                st.session_state[salvar_key] = len(df_presenca) > 0
            # decide colunas bloqueadas
            disabled_cols = ["nome"] if not st.session_state[salvar_key] else ["nome","presenca","biblia","revista"]
            
            if st.session_state[salvar_key]:
                tabela = pd.DataFrame(df_presenca)
                tabela = tabela[['nome', 'presenca','biblia','revista']].sort_values(by="nome").reset_index(drop=True)
                presentes = len(tabela[tabela['presenca'] == True])
                progresso = presentes / len(tabela)
                text_progresso = f'{progresso * 100: .2f}%'
                st.progress(progresso, text= f'{turma} {text_progresso}')
            else:
                tabela = df.sort_values(by="nome").reset_index(drop=True)

            if st.session_state[salvar_key]:
                st.success("Presenças salvas com sucesso!")

            # Editor retorna o df atualizado 
            edited_df = st.data_editor(tabela, disabled=disabled_cols, key=editor_key, hide_index=True) 

            # Botão salvar 
            if st.button("Salvar", key=f"btn_{turma}", disabled=st.session_state[salvar_key]): 
                st.session_state[salvar_key] = True
                edited_df["classe"] = turma 
                edited_df["data"] = hoje
                retorno = supabase.table('fct_presenca').select(
                    'nome','classe','presenca','data'
                    ).filter('data', 'eq', hoje).filter('classe','eq',turma).execute().data

                df_retorno = pd.DataFrame(retorno)
                if len(df_retorno) == 0:
                    supabase.table('fct_presenca').upsert( edited_df.to_dict(orient="records") ).execute()
                    st.success("Presenças salvas com sucesso!")
                
                presentes = len(edited_df[edited_df['presenca'] == True])
                progresso = presentes / len(edited_df)
                text_progresso = f'{progresso * 100: .2f}%'
                st.progress(progresso, text= f'{turma} {text_progresso}')
                    


#def inseredados(nome, classe, presenca):
#    data = {
#        'nome': nome,
#        'classe': classe,
#        'presenca': presenca
#    }

#    supabase.table('alunos').insert(data).execute()
