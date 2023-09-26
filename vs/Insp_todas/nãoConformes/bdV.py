#area de import onde importo as bibliotecas que vou utilizar
from datetime import datetime, timedelta
import mysql.connector
import pandas as pd
import win32com.client as win32
 
#aqui eu faço a conexao do codigo com o banco de dados
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='projetos',
)
cursor = conexao.cursor()
ontem = datetime.now().date()- timedelta(days= 5)
ontem_fm = ontem.strftime('%Y-%m-%d')
def inspseg(): 
    comando = f"""
    select * from InspSeg
    WHERE Resposta = 'NC'
    AND Data LIKE '{ontem_fm}%'
    """
    cursor.execute(comando)
    tudo = cursor.fetchall()
    data = pd.DataFrame(tudo)
    return data

def inspseg_lider(): 
    comando = f"""
    select * from projetos.is_lider
    WHERE Resposta = 'NC'
    AND Data LIKE '{ontem_fm}%'
    """
    cursor.execute(comando)
    tudo = cursor.fetchall()
    data = pd.DataFrame(tudo)
    return data
a = inspseg_lider()
print(a)
def vdiaria(): 
    comando = f"""
    select * from projetos.vdm
    WHERE Resposta = 'Pendente'
    AND date_ LIKE '{ontem_fm}%'
    """
    cursor.execute(comando)
    tudo = cursor.fetchall()
    data = pd.DataFrame(tudo)
    return data

b = vdiaria()
print(b)
