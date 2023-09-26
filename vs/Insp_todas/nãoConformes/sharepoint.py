from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import bdV
#region conexao sharepoint
# Informações do site do SharePoint
site_url = "https://gpssacombr.sharepoint.com"
username = "gabriel.mendes@gpssa.com.br"
password = "@1829GAjobeto"

# Nome da lista do SharePoint
list_name = "InspecaoSeg"



# Conectando-se ao site
authcookie = Office365(site_url, username=username, password=password).GetCookies()
site = Site('https://gpssacombr.sharepoint.com/sites/matheusegabriel1',authcookie=authcookie)
#endregion

# Obtendo a lista
lista = site.List(list_name)

df = bdV.inspseg()
if(len(df) == 0):
    print('Nenhuma pendencia hoje!')
else:
    for i in range(len(df)):
        id_sql = df.loc[i][0]
        cr = df.loc[i][10]
        cliente = df.loc[i][9]
        dataf = str(df.loc[i][1])
        pergunta = df.loc[i][3]
        disccr = df.loc[i][5]
        equipe = df.loc[i][6]
        id_est = df.loc[i][7]
        id_tarefa = df.loc[i][8]
        data = [
            {
            "id_sql": id_sql,
            "data": dataf,
            "pergunta": pergunta,
            "cr":cr,
            "equipe":equipe,
            "id_est":id_est,
            "id_tarefa":id_tarefa,
            "cliente":cliente,
            "disccr": disccr,
            # Adicione outras colunas e valores conforme necessário
            }
        ]
        lista.UpdateListItems(data, kind='New')
        print("EXECUTOU", i)
    print('nada fiote')


df_lider = bdV.inspseg_lider()
if(len(df_lider)== 0):
    print('Nenhuma pendencia hoje')
else:
    for i in range(len(df_lider)):
        id_sql = df_lider.loc[i][0]
        cr = df_lider.loc[i][10]
        cliente = df_lider.loc[i][9]
        dataf = str(df_lider.loc[i][1])
        pergunta = df_lider.loc[i][3]
        disccr = df_lider.loc[i][5]
        equipe = df_lider.loc[i][6]
        id_est = df_lider.loc[i][7]
        id_tarefa = df_lider.loc[i][8]
        data = [
            {
            "id_sql": id_sql,
            "data": dataf,
            "pergunta": pergunta,
            "cr":cr,
            "equipe":equipe,
            "id_est":id_est,
            "id_tarefa":id_tarefa,
            "cliente":cliente,
            "disccr": disccr,
            # Adicione outras colunas e valores conforme necessário
            }
        ]
        lista.UpdateListItems(data, kind='New')
        print("EXECUTOU", i)
    print('nada fiote')

df_vdiaria = bdV.vdiaria()
if(len(df_vdiaria)==0):
    print('Nada hoje')
else:
    for i in range(len(df_vdiaria)):
        id_sql = df_vdiaria.loc[i][0]
        cr = df_vdiaria.loc[i][10]
        cliente = df_vdiaria.loc[i][9]
        dataf = str(df_vdiaria.loc[i][1])
        pergunta = df_vdiaria.loc[i][3]
        disccr = df_vdiaria.loc[i][5]
        equipe = df_vdiaria.loc[i][6]
        id_est = df_vdiaria.loc[i][7]
        id_tarefa = df_vdiaria.loc[i][8]
        data = [
            {
            "id_sql": id_sql,
            "data": dataf,
            "pergunta": pergunta,
            "cr":cr,
            "equipe":equipe,
            "id_est":id_est,
            "id_tarefa":id_tarefa,
            "cliente":cliente,
            "disccr": disccr,
            # Adicione outras colunas e valores conforme necessário
            }
        ]
        lista.UpdateListItems(data, kind='New')
        print("EXECUTOU", i)
    print('nada fiote')
