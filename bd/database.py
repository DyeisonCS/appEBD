import streamlit as st
from supabase import create_client, Client
from bd import funcoes
import pandas as pd
import os
import datetime

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)



def database_segment():
    #st.header("🗄 Database", help="Testando criação de abas e paginas.")
    lista_alunos, cadastrar, turmas, ANIVERSARIANTES = \
        st.tabs(["Listar Alunos", "Cadastrar", "Turmas", "ANIVERSARIANTES"])
    
    with lista_alunos:
        if st.button('Listar Alunos'):
            #dados = funcoes.listardados()
            #tb = pd.DataFrame(dados, columns=['ID', 'nome', 'data_nasc', 'classe'])
            res = supabase.table('alunos').select('nome', 'classe').execute()
            st.write('Alunos:')   #header
            st.table(res.data)    
            #st.table(tb)

    with cadastrar:
        nome = st.text_input('Nome')
        data_nasc = st.date_input('Data Nascimento', datetime.date(1910, 1, 1), format="DD/MM/YYYY").strftime("%d/%m/%Y")
        classe = st.selectbox('Turma', options=['Vencedores por Cristos', 'Soldados de Cristo', 'Jardim de Deus', 'Joias de Cristo'], index=None, placeholder='Selecione')
        sexo = st.selectbox('Sexo', options=['masculino', 'feminino'], index=None, placeholder='Selecione')

        if st.button('cadastrar Aluno'):
            data = {
                'nome': nome,
                'data_nasc': data_nasc,
                'classe': classe
            }
            supabase.table('alunos').insert(data).execute()
            #funcoes.inseredados(nome, data_nasc, classe)
            st.success('Adicionado')



    with turmas:
        funcoes.tabturmas()

    with ANIVERSARIANTES:
        st.tabs(["Dyeison", "Rafael"])
    



