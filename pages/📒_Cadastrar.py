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


st.header('👤 Novo Aluno', text_alignment= 'left')

nome = st.text_input('Nome')
data_nasc = st.date_input('Data Nascimento', min_value= datetime.date(1910, 1, 1), format="DD/MM/YYYY").strftime("%d/%m/%Y")
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
