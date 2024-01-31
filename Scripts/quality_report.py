import pandas as pd 

tabela = pd.read_excel("Dados/Checklist QA Fic.xlsx")
dado = tabela.loc[tabela["Responsável"]=="Aegon VI Targaryen"]

# Do exemplo do vídeo tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador"] = 1.5
# Na coluna Tipo, nas linhas que possuem o item Serviço, altera a coluna Multiplicador para 1.5
# Não altera as outras linhas da tabela, só as que filtram certo como Serviço (não alterou as linhas com Produto, por exemplo)
print(dado)
