import streamlit as st
from supabase import create_client, Client
from bd import funcoes
import pandas as pd
import os
import datetime
from bd.banco import PresencaData
from utils.styles import inject_mobile_css

inject_mobile_css()

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)


def database_segment():
    inject_mobile_css()
    #st.header("🗄 Database", help="Testando criação de abas e paginas.")
    lista_alunos, ANIVERSARIANTES = \
        st.tabs(["Listar Alunos", "ANIVERSARIANTES"])
    
    with lista_alunos:
        diafiltro = st.date_input('Data Para Relatórios', min_value= datetime.date(2026, 1, 1), format="DD/MM/YYYY")
        res = PresencaData(diafiltro)
        tabela = pd.DataFrame(res)
        totalalunospresentes = len(tabela)

        if totalalunospresentes > 0:
            lista_unica = list(tabela['classe'].unique())
            if len(tabela) > 0:
                for turma in lista_unica:
                    #st.write(f'{turma}:')   #header
                    #st.table(res.data) 
                    #tabela = pd.DataFrame(res.data)
                    tabelafor = tabela[['nome', 'presenca', 'classe']].sort_values(by="nome").reset_index(drop=True)
                    tabelafiltrada = tabelafor[tabelafor['classe'] == turma]

                    presentes = len(tabelafiltrada[tabelafiltrada['presenca'] == True])
                    progresso = presentes / len(tabelafiltrada)
                    text_progresso = f'{progresso * 100: .2f}%'
                    st.progress(progresso, text= f'{turma} {text_progresso}')

        #if st.button('Listar Alunos'):
        #    #dados = funcoes.listardados()
        #    #tb = pd.DataFrame(dados, columns=['ID', 'nome', 'data_nasc', 'classe'])
        #    res = supabase.table('alunos').select('nome', 'classe').execute()
        #    st.write('Alunos:')   #header
        #    st.table(res.data)    
        #    #st.table(tb)


    


    with ANIVERSARIANTES:
        #st.tabs(["Dyeison", "Rafael"])
    



