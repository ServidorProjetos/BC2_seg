from sys import displayhook
import pyodbc
import pandas as pd
import split
from datetime import datetime, timedelta
# region Define a data para fazer o select
ontem = datetime.now().date() 
ontem_fm = ontem.strftime('%d/%m/%Y')
# endregion
def execute_select_with_retry(query, connection_string, max_attempts=10):

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
#region Defini a String de conexão
driver = 'SQL Server'; server='10.56.6.56'; database = 'DW_Vista '; username = 'matheus.pasquotti'; password = 'Matheus260105!'; trusted_connection ="no"
string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"
#endregion

def resposta(id_check):
    comando = f"""
            SELECT TarefaId, PerguntaOrdem, PerguntaDescricao, Conteudo 
            FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_FULL] 
            WHERE ChecklistId = '{id_check}' 
            AND Tipo = 1 
            AND PerguntaDescricao IS NOT NULL 
            AND CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' ORDER BY Data
            """
    Resposta = execute_select_with_retry(comando, string_conexao)
    return Resposta 

def data(id_check):
    comando = f"""
            SELECT Data 
            FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_FULL] 
            WHERE ChecklistId = '{id_check}' 
            AND Tipo = 1 
            AND PerguntaDescricao IS NOT NULL 
            AND CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' ORDER BY Data 
            """
    Resposta = execute_select_with_retry(comando, string_conexao)
    ddf = pd.DataFrame(Resposta)
    return ddf

def estrutura(id_est):
    est = f"""
        SELECT Nivel_03, Nivel_04, Cliente
        FROM  [DW_Vista].[dbo].[DM_ESTRUTURA] 
        where Id_Estrutura = '{id_est}'
        and Nivel_04 is not null
    """
    est = execute_select_with_retry(est,string_conexao)
    return est

def id(id_tarefa):
    est=f"""
        select Id_Estrutura from [DW_Vista].[dbo].[FT_Tarefa]
        where Id = '{id_tarefa}'
    """
    est = execute_select_with_retry(est,string_conexao)
    return est
