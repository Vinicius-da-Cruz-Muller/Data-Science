import pandas as pd 

tabela = pd.read_excel("Dados/Checklist QA Fic.xlsx")

#print(tabela)
#dado = tabela.loc[tabela["Responsável"]=="Aegon VI Targaryen"]

# Do exemplo do vídeo tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador"] = 1.5
# Na coluna Tipo, nas linhas que possuem o item Serviço, altera a coluna Multiplicador para 1.5
# Não altera as outras linhas da tabela, só as que filtram certo como Serviço (não alterou as linhas com Produto, por exemplo)
#print(dado)
def item1_1():
   #dado = tabela.loc[tabela["Nome ponto de decisão"].isin(["Execução", "Exec. Projeto"])] -----Funciona, filtra duas informações em uma coluna
   #dado = tabela.loc[tabela["Nome ponto de decisão"].isin(["Execução", "Exec. Projeto"]) & tabela["Data real de início"].isnull()]
   dado = tabela.loc[tabela["Nome ponto de decisão"].isin(["Execução", "Exec. Projeto"]) & tabela["Data real de início"].isnull() | tabela["Dt.real in.pto.dec"].isnull()]
   print(dado)
   
item1_1()

def item1_2():
   dado = tabela.loc[tabela["Nome ponto de decisão"].isin(["Exec. Business Case"])& tabela["Dt.real in.pto.dec"].isnull()]
   print(dado)

item1_2()
# colunas = tabela.columns 
# print(colunas)