import requests
from msal import ConfidentialClientApplication

# Configurações
client_id = 'seu_client_id'
client_secret = 'seu_client_secret'
authority = 'https://login.microsoftonline.com/seu_tenant_id'
scope = ["https://analysis.windows.net/powerbi/api/.default"]
report_id = 'id_do_seu_relatorio'

# Inicialização do aplicativo confidencial
app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# Autenticação e obtenção do token de acesso
token_response = app.acquire_token_silent(scope, account=None)
if not token_response:
    token_response = app.acquire_token_for_client(scopes=scope)

if "access_token" in token_response:
    access_token = token_response["access_token"]
else:
    raise ValueError("Não foi possível obter o token de acesso.")

# Atualização do relatório
update_url = f'https://api.powerbi.com/v1.0/myorg/reports/{report_id}/Rebind'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

update_data = {
    "datasetId": "id_do_seu_conjunto_de_dados",
    "defaultRetentionPolicy": "retainAllData"
}

response = requests.post(update_url, headers=headers, json=update_data)

if response.status_code == 200:
    print("Relatório atualizado com sucesso!")
else:
    print("Ocorreu um erro ao atualizar o relatório.")
    print(response.text)
