from sys import displayhook
import pyodbc
import pandas as pd
import split 
from datetime import datetime, timedelta

ontem = datetime.now().date() - timedelta(days= 2) 
ontem_fm = ontem.strftime('%d/%m/%Y')

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

# Exemplo de uso
driver = 'SQL Server'; server='10.56.6.56'; database = 'DW_Vista '; username = 'gabriel.mendes'; password = 'Grupogps@12345'; trusted_connection ="no"
string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

#id tarefa 
tarefa_id = f"SELECT TarefaId FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'cliente' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Itarefa_id = execute_select_with_retry(tarefa_id, string_conexao)
Itarefa_id = pd.DataFrame(Itarefa_id)

#Contrato
Rcontrato = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Contrato' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Icontrato= execute_select_with_retry(Rcontrato, string_conexao)
Icontrato = pd.DataFrame(Icontrato)

#atividade
Ratividade = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Atividade' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iatividade = execute_select_with_retry(Ratividade, string_conexao)
Iatividade = pd.DataFrame(Iatividade)
# print(Iatividade)

#Tarefa
Rtarefa = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Tarefa' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Itarefa = execute_select_with_retry(Rtarefa, string_conexao)
Itarefa = pd.DataFrame(Itarefa)
# print(Itarefa)

#função
Rfuncao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Função' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Ifuncao = execute_select_with_retry(Rfuncao, string_conexao)
Ifuncao = pd.DataFrame(Ifuncao)
# print(Ifuncao)

#Perigo
Rperigo = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Perigo' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iperigo = execute_select_with_retry(Rperigo, string_conexao)
Iperigo = pd.DataFrame(Iperigo)
# print(Iperigo)

#Condição do perigo
RcondicaoPerigo = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Condição Do Perigo' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
IcondicaoPerigo = execute_select_with_retry(RcondicaoPerigo, string_conexao)
IcondicaoPerigo = pd.DataFrame(IcondicaoPerigo)

#risco
Rrisco = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Risco' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Irisco = execute_select_with_retry(Rrisco, string_conexao)
Irisco = pd.DataFrame(Irisco)

#Dano
Rdano = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Dano' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Idano = execute_select_with_retry(Rdano, string_conexao)
Idano = pd.DataFrame(Idano)

#Quantidade de Pessoas Expostas
Rqpe = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Quantidade de Pessoas Expostas' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iqpe = execute_select_with_retry(Rqpe, string_conexao)
Iqpe = pd.DataFrame(Iqpe)

#Severidade
Rseveridade = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Severidade' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iseveridade = execute_select_with_retry(Rseveridade, string_conexao)
Iseveridade_df = pd.DataFrame(Iseveridade)

#Exposição
Rexposicao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Exposição' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iexposicao = execute_select_with_retry(Rexposicao, string_conexao)
Iexposicao_df = pd.DataFrame(Iexposicao)

#Probabilidade
Rprobabilidade = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Probabilidade' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iprobabilidade = execute_select_with_retry(Rprobabilidade, string_conexao)
Iprobabilidade_df = pd.DataFrame(Iprobabilidade)

#Eliminacao
Reliminacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Física - Eliminação ' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Ieliminacao = execute_select_with_retry(Reliminacao, string_conexao)
Ieliminacao = pd.DataFrame(Ieliminacao)

#Statos Eliminacao
Rseliminacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Eliminação' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iseliminacao = execute_select_with_retry(Rseliminacao, string_conexao)
Iseliminacao = pd.DataFrame(Iseliminacao)

#Redução
Rreducao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Física - Redução' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Ireducao = execute_select_with_retry(Rreducao, string_conexao)
Ireducao = pd.DataFrame(Ireducao)

#Status Redução
Rsreducao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Redução' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isreducao = execute_select_with_retry(Rsreducao, string_conexao)
Isreducao = pd.DataFrame(Isreducao)


#Interceptação
Rinterceptacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Física - Interceptação' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iinterceptacao = execute_select_with_retry(Rinterceptacao, string_conexao)
Iinterceptacao = pd.DataFrame(Iinterceptacao)

#Status Interceptação
Rsinterceptacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Interceptação' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isinterceptacao = execute_select_with_retry(Rsinterceptacao, string_conexao)
Isinterceptacao = pd.DataFrame(Isinterceptacao)


#Advertencia
Radvertencia = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191' and PerguntaDescricao = 'Sistêmica - Advertência' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iadvertencia = execute_select_with_retry(Radvertencia, string_conexao)
Iadvertencia = pd.DataFrame(Iadvertencia)

#Status Advertencia
Rsadvertencia = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Advertência' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isadvertencia = execute_select_with_retry(Rsadvertencia, string_conexao)
Isadvertencia = pd.DataFrame(Isadvertencia)


#verificacao
Rverificacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Sistêmica - Verificação' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iverificacao = execute_select_with_retry(Rverificacao, string_conexao)
Iverificacao = pd.DataFrame(Iverificacao)

#Statos verificacao
Rsverificacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira  - Verificação' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isverificacao = execute_select_with_retry(Rsverificacao, string_conexao)
Isverificacao = pd.DataFrame(Isverificacao)

#Conscientização
Rconscientizacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Sistêmica - Conscientização' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iconscientizacao = execute_select_with_retry(Rconscientizacao, string_conexao)
Iconscientizacao = pd.DataFrame(Iconscientizacao)

#Statos Conscientização
Rsconscientizacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Conscientização' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isconscientizacao = execute_select_with_retry(Rsconscientizacao, string_conexao)
Isconscientizacao = pd.DataFrame(Isconscientizacao)


#Padronização
Rpadronizacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Sistêmica - Padronização' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Ipadronizacao = execute_select_with_retry(Rpadronizacao, string_conexao)
Ipadronizacao = pd.DataFrame(Ipadronizacao)

#Statos Padronização
Rspadronizacao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Padronização' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Ispadronizacao = execute_select_with_retry(Rspadronizacao, string_conexao)
Ispadronizacao = pd.DataFrame(Ispadronizacao)

#EPI
Repi = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Comportamental - EPI' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iepi = execute_select_with_retry(Repi, string_conexao)
Iepi = pd.DataFrame(Iepi)

#Statos EPI
Rsepi = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - EPI' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isepi = execute_select_with_retry(Rsepi, string_conexao)
Isepi = pd.DataFrame(Isepi)

#Supervisão
Rsupervisao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Comportamental - Supervisão' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isupervisao = execute_select_with_retry(Rsupervisao, string_conexao)
Isupervisao = pd.DataFrame(Isupervisao)

#Statos Supervisão
Rssupervisao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Supervisão' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Issupervisao = execute_select_with_retry(Rssupervisao, string_conexao)
Issupervisao = pd.DataFrame(Issupervisao)

#Atenção
Ratencao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Comportamental - Atenção' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iatencao = execute_select_with_retry(Ratencao, string_conexao)
Iatencao = pd.DataFrame(Iatencao)

#Statos Atenção
Rsatencao = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Situação da Barreira - Atenção' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Isatencao = execute_select_with_retry(Rsatencao, string_conexao)
Isatencao = pd.DataFrame(Isatencao)

#Ação de Contenção
Rac = f"SELECT Conteudo FROM [DW_Vista].[dbo].[FT_CHECKLIST_RESPOSTA_SEGURANCA] where CheckListId = 'aec39461-d4ab-4e41-89cd-49e8a34c1191'  and PerguntaDescricao = 'Ação de Contenção' and CONVERT(varchar, Data, 103) LIKE '{ontem_fm}%' order by Data"
Iac = execute_select_with_retry(Rac, string_conexao)
Iac = pd.DataFrame(Iac)
