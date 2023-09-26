import mysql.connector
import pandas as pd
# import BD_Vista
import math

from datetime import date, timedelta

# Obter a data atual
atual = date.today()

# Calcular a data daqui a 30 dias
data_futura = (atual + timedelta(days=30))

# Calcular 'Fora do padrão'
data_fp = data_futura + timedelta(days=5)


conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='projetos',
)
cursor = conexao.cursor()

cursor = conexao.cursor()   
def distancia_entre_coordenadas(lat1, lon1, lat2, lon2):
    # Função para calcular a distância entre duas coordenadas (latitude, longitude)
    # usando a fórmula de Haversine.
    R = 6371  # Raio médio da Terra em km
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) * math.sin(d_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia
def verificar_proximidade(coord1, coord2, margem):
    distancia_entre_coords = distancia_entre_coordenadas(coord1[0], coord1[1], coord2[0], coord2[1])
    
    if distancia_entre_coords <= margem:
        km = f"select Km from KmRodoviaSul where Latitude like '%{latitude}%'"
        cursor.execute(km)
        km = cursor.fetchall()
        km = str(km).split(",")
        km = km[0].split("(")
        km = int(km[1])
        return km
    else:
        return 'Nada'

ltelg = f"Select Latitude, Longitude from KmRodoviaNorte where Rodovia = 'MS-306'"
cursor.execute(ltelg)
ltelg = cursor.fetchall()
ltelg = pd.DataFrame(ltelg)
print('oto aki')
for i in range(len(ltelg)):
    Ltelg = str(ltelg.loc[i]).split('\n')
    lt_sql = str(Ltelg[0]).split()
    lt_sql = lt_sql[1]
    latitude = lt_sql
    lt_sql = str(lt_sql).replace(',','.')
    lg_sql = str(Ltelg[1]).split()
    lg_sql = str(lg_sql[1]).replace(',','.')

    crd_sql = (float(lt_sql), float(lg_sql))  # Coordenada específica 1
    crd_i = (-18.041693 ,-53.155341)  # Coordenada específica 2
    margem_proximidade_km = 0.5  # Aproximadamente 500 metros em quilômetros
    kminicial = verificar_proximidade(crd_sql, crd_i, margem_proximidade_km)
    if kminicial != 'Nada':
        kmi = kminicial
        print('funk')

for i in range(len(ltelg)):
    Ltelg = str(ltelg.loc[i]).split('\n')
    lt_sql = str(Ltelg[0]).split()
    lt_sql = lt_sql[1]
    latitude = lt_sql
    lt_sql = str(lt_sql).replace(',','.')
    lg_sql = str(Ltelg[1]).split()
    lg_sql = str(lg_sql[1]).replace(',','.')

    crd_sql = (float(lt_sql), float(lg_sql))  # Coordenada específica 1
    margem_proximidade_km = 0.5  # Aproximadamente 500 metros em quilômetros
    crd_f = (-18.130409 ,-53.137622) 
    kmFinal = verificar_proximidade(crd_sql, crd_f, margem_proximidade_km)
    if kmFinal != 'Nada':
        kmfim = kmFinal
        print('FUCK')

print(kmfim)
print(kmi)
stUP = f"UPDATE projetos.KmRodoviaNorte SET Statos = 'Realizado', DataR = '{atual}', DataVencimento = '{data_futura}', DataForaP = '{data_fp}' WHERE Rodovia = 'MS-306' and Km between {kmi} AND {kmfim}" 
cursor.execute(stUP)
conexao.commit()
print(stUP)
print('Atualizado')   


cursor.close()
conexao.close()