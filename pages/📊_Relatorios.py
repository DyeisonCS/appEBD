import streamlit as st
import datetime
import pandas as pd
from bd import banco
from utils.styles import inject_mobile_css

inject_mobile_css()

st.header('📊 Relatórios')

inicio = datetime.date(2026, 1, 1)
fim = datetime.date.today()

# slider para escolher intervalo
data_inicio, data_fim = st.slider(
    "Selecione o Período do Relatório",
    min_value=inicio,
    max_value=fim,
    value=(inicio, fim),
    format="DD/MM/YYYY"
)

tabela = pd.DataFrame(banco.RelatorioPresencaTurma(data_inicio, data_fim))
lista_unica = list(tabela['classe'].unique())
lista_dias = list(tabela['data'].unique())

qtde_dias = len(lista_dias)

turmaselecionada = st.selectbox('Turma:', options= lista_unica)
df_classe_selecionada = tabela[tabela["classe"] == turmaselecionada]

qtde_presencas = df_classe_selecionada.groupby('nome', as_index=False)['presenca'].sum()
qtde_presencas['presenca'] = qtde_presencas['presenca'].astype(int) / qtde_dias

qtde_presencas['presenca'] = qtde_presencas['presenca'] * 100

st.data_editor(qtde_presencas,
               hide_index= True,
               column_config={
                   'presenca':st.column_config.ProgressColumn(
                       min_value=0,
                       max_value=100,
                       format="%.1f%%"
                   )
               }

)
