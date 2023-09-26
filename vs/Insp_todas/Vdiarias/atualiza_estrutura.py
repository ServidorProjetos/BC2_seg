import mysql.connector
import pandas as pd
import bdv
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='projetos',
)
cursor = conexao.cursor()

comando = f"""
    SELECT distinct id_tar FROM projetos.vdm
    where id_est is null
"""
cursor.execute(comando)
idtarefas = cursor.fetchall()

if len(idtarefas) == 0:
    print('Atualizado')
else:
    for i in range(len(idtarefas)):
        ids = str(idtarefas[i]).split("'")
        id_tarefa = ids[1]
        est = bdv.id(id_tarefa)
        id_estr = str(est).split("'")
        id_est = id_estr[1]
        comando = f"""
            UPDATE projetos.vdm
            SET id_est = ('{id_est}')
            WHERE id_tar = '{id_tarefa}';
            """
        cursor.execute(comando)
        conexao.commit()

