from datetime import date, timedelta
import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='projetos',
)
cursor = conexao.cursor()

cursor = conexao.cursor() 

# Obter a data atual
atual = date.today()
# Calcular a data daqui a 30 dias
data_futura = (atual + timedelta(days=30))
# Calcular 'Fora do padrão'
data_fp = data_futura + timedelta(days=5)

print(f'''{atual}
{data_futura}
{data_fp}''')

dataP = f"UPDATE projetos.KmRodoviaNorte SET Statos = 'Período de retorno' WHERE DataVencimento = '{atual}' "
cursor.execute(dataP)
conexao.commit()

dataF = f"UPDATE projetos.KmRodoviaNorte SET Statos = 'Fora do padrão' WHERE DataForaP = '{atual}' "
cursor.execute(dataF)
conexao.commit()