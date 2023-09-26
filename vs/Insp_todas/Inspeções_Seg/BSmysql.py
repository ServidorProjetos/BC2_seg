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
def inserir_dados(id_t):

    ontem_fm = bdv.ontem.strftime('%Y-%m-%d')

    comando_verificacao = f"""
    SELECT COUNT(*) FROM `projetos`.`InspSeg` WHERE Id_Tarefa = '{id_t}'
    and Pergunta = '{pergunta}' 
    and Data = '{ontem_fm}'
    """
    cursor.execute(comando_verificacao)
    resultado = cursor.fetchone()
    if resultado[0] == 0:
        comando = """
        INSERT INTO `projetos`.`InspSeg` (`Data`, `PerguntaOrdem`, `Pergunta`, `Resposta`, `Id_Tarefa`)
        VALUES (%s, %s, %s, %s, %s)
        """
        dados = (dataf, perguntaOrdem[1], pergunta, conteudo, id_terefa)
        cursor.execute(comando, dados)
        conexao.commit()
    

# Conecte-se ao banco de dados usando o contexto
respostas = bdv.resposta()
data = bdv.data()
for i in range(len(respostas)):
    dataf = str(data.loc[i]).split(" ")[4].split("[")[1]
    allitems = str(respostas[i]).split("'")
    id_terefa = allitems[1]
    pergunta = allitems[3]
    conteudo = allitems[5]
    perguntaOrdem = allitems[2].strip().split(',')
    inserir_dados(id_terefa)


