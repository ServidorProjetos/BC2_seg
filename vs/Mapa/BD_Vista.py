from sys import displayhook
import pyodbc
import pandas as pd
import split 
from datetime import datetime, timedelta

ontem = datetime.now().date() - timedelta(days= 1)
ontem_fm = ontem.strftime('%d/%m/%Y')

#Metodo de conexao ao BANCO DE DADOS DO VISTA
driver = 'SQL Server'; server='10.56.6.56'; database = 'DW_Vista '; username = 'gabriel.mendes'; password = 'Grupogps@12345'; trusted_connection ="no"
string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

def ex(query, connection_string, max_attempts=4):
    for attempt in range(1, max_attempts + 1):
        try:
            with pyodbc.connect(connection_string) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    return results
        except pyodbc.Error as e:
            print(f"Tentativa {attempt} falhou: {e}")
            if attempt < max_attempts:
                print("Tentando novamente...")
            else:
                print("Máximo de tentativas alcançado. Não foi possível executar o SELECT.")
                return None


rodovia = f"select Conteudo from [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where ChecklistId = 'c51cb1f1-0849-43ae-9bd2-ad99c4f3d57d' and PerguntaDescricao = 'Rodovia' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data" 
rodovia = ex(rodovia, string_conexao)
rodovia =pd.DataFrame(rodovia)

NS = f"select Conteudo from [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where ChecklistId = 'c51cb1f1-0849-43ae-9bd2-ad99c4f3d57d' and PerguntaDescricao = 'Indique o sentido que vai ser ou foi percorrido (Norte de Baixo para Cima, segundo o maps)(Sul de Cima para Baixo).' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data" 
ns = ex(NS, string_conexao)
ns =pd.DataFrame(ns)

#puxa a latitude inicial
lt_i = (f"SELECT [Latitude_I] FROM [DW_Vista].[dbo].[DM_EXECUCAO] where ChecklistId = 'c51cb1f1-0849-43ae-9bd2-ad99c4f3d57d' and CONVERT(varchar, Data_F, 103) LIKE '{ontem_fm}%' order by Data_F")        
lt_i = ex(lt_i, string_conexao)
lt_i = pd.DataFrame(lt_i)


#Puxa longitude inicial
lg_i = (f"SELECT [Longitude_I] FROM [DW_Vista].[dbo].[DM_EXECUCAO] where ChecklistId = 'c51cb1f1-0849-43ae-9bd2-ad99c4f3d57d' and CONVERT(varchar, Data_F, 103) LIKE '{ontem_fm}%' order by Data_F ")        
lg_i = ex(lg_i, string_conexao) 
lg_i = pd.DataFrame(lg_i)


#puxa a latitude final
lt_f = (f"SELECT [Latitude_F] FROM [DW_Vista].[dbo].[DM_EXECUCAO] where ChecklistId = 'c51cb1f1-0849-43ae-9bd2-ad99c4f3d57d' and CONVERT(varchar, Data_F, 103) LIKE '{ontem_fm}%' order by Data_F")
lt_f = ex(lt_f, string_conexao)
lt_f= pd.DataFrame(lt_f)


#Puxa longitude final
lg_f = (f"SELECT [Longitude_F] FROM [DW_Vista].[dbo].[DM_EXECUCAO] where ChecklistId = 'c51cb1f1-0849-43ae-9bd2-ad99c4f3d57d' and CONVERT(varchar, Data_F, 103) LIKE '{ontem_fm}%' order by Data_F")
lg_f= ex(lg_f, string_conexao)
lg_f = pd.DataFrame(lg_f)