import streamlit as st
import pandas as pd
from bd import funcoes
from supabase import create_client, Client
import os

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)


st.set_page_config(
    page_icon= 'logo_ipb.png',
    page_title= 'EBD IPSO'
)

st.title('Cadastro de Aluno Escola Biblica Dominical') #write

nome = st.text_input('Nome')
data_nasc = st.date_input('Data Nascimento', format="DD/MM/YYYY").strftime("%d/%m/%Y")
classe = st.selectbox('Turma', options=['Vencedores por Cristos', 'Soldados de Cristo', 'Jardim de Deus', 'Joias de Cristo'], index=None, placeholder='Selecione')
sexo = st.selectbox('Sexo', options=['masculino', 'feminino'], index=None, placeholder='Selecione')

if st.button('Adicionar Aluno'):
    data = {
        'nome': nome,
        'data_nasc': data_nasc,
        'classe': classe
    }
    supabase.table('alunos').insert(data).execute()
    #funcoes.inseredados(nome, data_nasc, classe)
    st.success('Adicionado')

if st.button('Listar Alunos'):
    #dados = funcoes.listardados()
    #tb = pd.DataFrame(dados, columns=['ID', 'nome', 'data_nasc', 'classe'])
    res = supabase.table('alunos').select('*').execute()
    st.write('Alunos:')   #header
    st.table(res.data)    
    #st.table(tb)  