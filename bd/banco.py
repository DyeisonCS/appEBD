from supabase import create_client, Client


#url = os.environ["SUPABASE_URL"]
#key = os.environ["SUPABASE_KEY"]
#supabase = create_client(url, key)

url = "https://vncdlatpuvniwwzdebtb.supabase.co"
key = "sb_publishable_X5t9KZPR-0LJZF0BaMRT5w_rmhCUW6h"
supabase: Client = create_client(url, key)

###Selecionar todas as presenças do dia, criar uma variável com a data que deseja retornar as presenças
def PresencaData(data):
    res = supabase.table('fct_presenca').select('nome', 'classe', 'presenca').filter('data', 'eq', data).execute()
    return res.data