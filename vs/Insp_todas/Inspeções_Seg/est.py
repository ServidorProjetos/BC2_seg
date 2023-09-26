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
    SELECT distinct Id_Est FROM projetos.InspSeg
        where DescCR is null 
        or Equipe is null
        or Cliente is null
"""
cursor.execute(comando)
allids = cursor.fetchall()

if len(allids) == 0:
    print('Atualizado')
else:
    for i in range(len(allids)):
        id_est = str(allids[i]).split("'")
        id_estrutura = id_est[1]
        est = bdv.estrutura(id_estrutura)
        allitems = str(est).split("'")
        descCR = allitems[1]
        equipe = allitems[3]
        client = allitems[5].split(" ")[2]
        cr = allitems[1].split(" ")[0]
        comando = f"""
            UPDATE `projetos`.`InspSeg`
            SET DescCR = ('{descCR}'), Equipe = ('{equipe}'), Cliente = ('{client}'), cr = ('{cr}')
            WHERE Id_Est = '{id_estrutura}';
        """
        cursor.execute(comando)
        conexao.commit()
