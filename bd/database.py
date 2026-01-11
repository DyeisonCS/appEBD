import streamlit as st
from supabase import create_client, Client
import os

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)



def database_segment():
    #st.header("🗄 Database", help="Testando criação de abas e paginas.")
    lista_alunos, cadastrar, drop_tab, describe_tab, show_tab, ANIVERSARIANTES, tips_tab = \
        st.tabs(["Listar Alunos", "Cadastrar", "DROP", "DESCRIBE", "SHOW", "ANIVERSARIANTES", "❄️"])
    
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
        data_nasc = st.date_input('Data Nascimento', format="DD/MM/YYYY").strftime("%d/%m/%Y")
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



    with drop_tab:
        st.button('Teste Drop')

    with describe_tab:
        st.button('Teste Describe')

    with show_tab:
        st.button('Teste Show')
    
    with ANIVERSARIANTES:
        st.tabs(["Dyeison", "Rafael"])

    with tips_tab:
    
        st.markdown("""
        💡 **Tips**
        - Follow consistent and meaningful naming conventions for `DATABASE` objects.
        - When you create a new Snowflake database, it also generates two schemas: `PUBLIC` (the default schema) and `INFORMATION_SCHEMA` (containing views and table functions for querying metadata across objects).
        - Use a `TRANSIENT` `DATABASE` to isolate temporary data, and provide a dedicated space for intermediate results or temporary tables during specific analysis or transformation tasks.
        - Utilize zero-copy cloning using `CREATE DATABASE <name> CLONE <source_db>` for efficient, space-saving `DATABASE` copies.
        - Continuously analyze query and resource usage patterns to fine-tune `DATABASE` parameters for optimal performance and cost efficiency.
        """
        )
    

