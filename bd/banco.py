from supabase import create_client, Client
import os


url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

###Selecionar todas as presenças do dia, criar uma variável com a data que deseja retornar as presenças
def PresencaData():
    res = supabase.table('fct_presenca').select('nome', 'classe', 'presenca', 'data').execute()
    return res.data


def RelatorioPresencaTurma(inicio, fim):
    res = supabase.table('fct_presenca').select('nome', 'classe', 'presenca', 'data').filter('data', 'gte', inicio).filter('data', 'lte', fim).execute()
    return res.data

