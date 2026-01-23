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
    Resumo, ANIVERSARIANTES = \
        st.tabs(["Resumo", "ANIVERSARIANTES"])
    
    with Resumo:
        #diafiltro = st.date_input('Data Nascimento', min_value= datetime.date(2026, 1, 1), format="DD/MM/YYYY")
        res = PresencaData()
        tabelacompleta = pd.DataFrame(res)
        totalalunospresentes = len(tabelacompleta)

        dias_semana = { 
            0: "Segunda-feira",
            1: "Terça-feira",
            2: "Quarta-feira",
            3: "Quinta-feira",
            4: "Sexta-feira",
            5: "Sábado",
            6: "Domingo",
        }

        if totalalunospresentes > 0:
            lista_unica = list(tabelacompleta['data'].unique())

            for dia in lista_unica:
                datafor = datetime.date.fromisoformat(dia)
                datadia = dias_semana[datafor.weekday()]
                tabelacompleta["data"] = pd.to_datetime(tabelacompleta["data"]).dt.date
                tabela = tabelacompleta[tabelacompleta['data'] == datafor]

                presentes = tabela['presenca'].sum()
                #st.data_editor(tabela, key=dia)

                with st.expander(f'📆 {datafor.strftime("%d/%m/%Y")} {datadia}:'): 
                    #st.write(presentes)
                    lista_unica = list(tabela['classe'].unique())
                    for turma in lista_unica:
                        tabelafor = tabela[['nome', 'presenca', 'classe']].sort_values(by="nome").reset_index(drop=True)
                        tabelafiltrada = tabelafor[tabelafor['classe'] == turma]

                        presentes = len(tabelafiltrada[tabelafiltrada['presenca'] == True])
                        progresso = presentes / len(tabelafiltrada)
                        text_progresso = f'{progresso * 100: .2f}%'
                        st.progress(progresso, text= f'{turma} {text_progresso}')
    


    with ANIVERSARIANTES:
        st.tabs(["Dyeison", "Rafael"])
    






