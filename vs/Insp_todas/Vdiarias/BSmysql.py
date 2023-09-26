import mysql.connector
import id_list
import pandas as pd
import bdv
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='projetos',
)
cursor = conexao.cursor()

def inserir_dados(id_t,insp):

    ontem_fm = bdv.ontem.strftime('%Y-%m-%d')

    comando_verificacao = f"""
    SELECT COUNT(*) FROM projetos.vdm WHERE id_tar = '{id_t}'
    and pergunta = '{pergunta}' 
    and date_ = '{ontem_fm}'
    """
    cursor.execute(comando_verificacao)
    resultado = cursor.fetchone()
    if resultado[0] == 0:
        comando = """
        INSERT INTO projetos.vdm (`date_`, `inspecao`, `perg_ordem`, `pergunta`, `resposta`, `id_tar`)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        dados = (dataf, insp, perguntaOrdem[1], pergunta, conteudo, id_terefa)
        cursor.execute(comando, dados)
        conexao.commit()


#region VEICULO
respostas = bdv.resposta(id_list.veiculo)
data = bdv.data(id_list.veiculo)
for i in range(len(respostas)):
    insp = 'VEICULO'
    dataf = str(data.loc[i]).split(" ")[4].split("[")[1]
    allitems = str(respostas[i]).split("'")
    id_terefa = allitems[1]
    pergunta = allitems[3]
    conteudo = allitems[5]
    perguntaOrdem = allitems[2].strip().split(',')
    inserir_dados(id_terefa,insp)
#endregion

# #region MOTOSSERRA
respostas = bdv.resposta(id_list.motosserra)
data = bdv.data(id_list.motosserra)
for i in range(len(respostas)):
    insp = 'MOTOSSERRA'
    dataf = str(data.loc[i]).split(" ")[4].split("[")[1]
    allitems = str(respostas[i]).split("'")
    id_terefa = allitems[1]
    pergunta = allitems[3]
    conteudo = allitems[5]
    perguntaOrdem = allitems[2].strip().split(',')
    inserir_dados(id_terefa,insp)
# #endregion

# #region MOTOPODA
respostas = bdv.resposta(id_list.motopoda)
data = bdv.data(id_list.motopoda)
for i in range(len(respostas)):
    insp = 'MOTOPODA'
    dataf = str(data.loc[i]).split(" ")[4].split("[")[1]
    allitems = str(respostas[i]).split("'")
    id_terefa = allitems[1]
    pergunta = allitems[3]
    conteudo = allitems[5]
    perguntaOrdem = allitems[2].strip().split(',')
    inserir_dados(id_terefa,insp)
# #endregion

# #region ROÇADEIRA
respostas = bdv.resposta(id_list.roçadeira)
data = bdv.data(id_list.roçadeira)
for i in range(len(respostas)):
    insp = 'ROÇADEIRA'
    dataf = str(data.loc[i]).split(" ")[4].split("[")[1]
    allitems = str(respostas[i]).split("'")
    id_terefa = allitems[1]
    pergunta = allitems[3]
    conteudo = allitems[5]
    perguntaOrdem = allitems[2].strip().split(',')
    inserir_dados(id_terefa, insp)
# #endregion