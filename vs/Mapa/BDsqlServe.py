import mysql.connector
import pandas as pd
import BD_Vista
import Calc_Data
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


# loop para percorrer todas as respostas que foram retidas do Vista
for i in range(len(BD_Vista.rodovia)):
    #Nome da Rodovia
    rodovia = str(BD_Vista.rodovia.loc[i]).split('[')
    rodovia = rodovia[1].split(']')
    rodovia = str(rodovia[0])    
    #sentido da via (Norte/Sul)
    ns = str(BD_Vista.ns.loc[i]).split('[')
    ns = ns[1].split(']')
    ns = str(ns[0])    
    #latitude inicial
    lt_i = str(BD_Vista.lt_i.loc[i]).split('[')
    lt_i = lt_i[1].split(']')
    lt_i = lt_i[0]
    #longitude inicial
    lg_i = str(BD_Vista.lg_i.loc[i]).split('[')
    lg_i = lg_i[1].split(']')
    lg_i = lg_i[0]
    #latitude final
    lt_f = str(BD_Vista.lt_f.loc[i]).split('[')
    lt_f = lt_f[1].split(']')
    lt_f = lt_f[0]
    #longitude final
    lg_f = str(BD_Vista.lg_f.loc[i]).split('[')
    lg_f = lg_f[1].split(']')
    lg_f = lg_f[0]
    
    # difine se é norte ou sul para dar update no bd certo
    if ns == 'Norte':
        ltelg = f"Select Latitude, Longitude from KmRodoviaNorte where Rodovia = '{rodovia}'"
        cursor.execute(ltelg)
        ltelg = cursor.fetchall()
        ltelg = pd.DataFrame(ltelg)
        for i in range(len(ltelg)):
            Ltelg = str(ltelg.loc[i]).split('\n')
            lt_sql = str(Ltelg[0]).split()
            lt_sql = lt_sql[1]
            latitude = lt_sql
            lt_sql = str(lt_sql).replace(',','.')
            lg_sql = str(Ltelg[1]).split()
            lg_sql = str(lg_sql[1]).replace(',','.')
            crd_sql = (float(lt_sql), float(lg_sql))  # Coordenada específica 1
            crd_i = (lt_i,lg_i)  # Coordenada específica 2
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
            crd_f = (lt_f, lg_f) 
            kmFinal = verificar_proximidade(crd_sql, crd_f, margem_proximidade_km)
            if kmFinal != 'Nada':
                kmfim = kmFinal
                print('FUCK')

        print(kmfim)
        print(kmi)
        stUP = f"UPDATE projetos.KmRodoviaNorte SET Statos = 'Realizado', DataR = '{atual}', DataVencimento = '{data_futura}', DataForaP = '{data_fp}' WHERE Rodovia = 'MS-306' and Km between {kmi} AND {kmfim}" 
        cursor.execute(stUP)
        conexao.commit()

    else:
        ltelg = f"Select Latitude, Longitude from KmRodoviaSul where Rodovia = '{rodovia}'"
        cursor.execute(ltelg)
        ltelg = cursor.fetchall()
        ltelg = pd.DataFrame(ltelg)
        for i in range(len(ltelg)):
            Ltelg = str(ltelg.loc[i]).split('\n')
            lt_sql = str(Ltelg[0]).split()
            lt_sql = lt_sql[1]
            latitude = lt_sql
            lt_sql = str(lt_sql).replace(',','.')
            lg_sql = str(Ltelg[1]).split()
            lg_sql = str(lg_sql[1]).replace(',','.')

            crd_sql = (float(lt_sql), float(lg_sql))  # Coordenada específica 1
            crd_i = (lt_i, lg_i)  # Coordenada específica 2
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
            crd_f = (lt_f, lg_f)  
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
        
cursor.close()
conexao.close()