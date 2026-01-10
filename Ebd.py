import streamlit as st
import pandas as pd
from bd import funcoes

st.write('Cadastro de Aluno Escola Biblica Dominical')

nome = st.text_input('Nome')
data_nasc = st.text_input('data_nasc')
classe = st.text_input('classe')

if st.button('Adicionar Aluno'):
    funcoes.inseredados(nome, data_nasc, classe)
    st.success('Adicionado')

if st.button('listar clientes'):
    dados = funcoes.listardados()
    tb = pd.DataFrame(dados, columns=['ID', 'nome', 'data_nasc', 'classe'])
    st.header('Alunos')
    st.table(tb)