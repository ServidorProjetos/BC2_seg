from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import mysql.connector
import win32com.client as win32
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='projetos',
)
cursor = conexao.cursor()
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
items = lista.GetListItems()

for item in items:
    feito = item.get('feito', '')

    if feito == 'S':
        id_sql = item.get('id_sql','')
        comando = f"""
                UPDATE `projetos`.`InspSeg` 
                SET `Resposta` = 'C' 
                WHERE (`id` = '{id_sql}');
            """
        cursor.execute(comando)
        conexao.commit()
        print('EXECUTOU')
