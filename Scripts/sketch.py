import pandas as pd 

tabela = pd.read_excel("Dados/Checklist QA Fic.xlsx")


# from tkinter import *

# def item2():
#     # Definindo as colunas que serão impressas
#     colunas = ["Nome ponto de decisão", "Dt. Plan início", "Data real de início", "Status ponto de decisão"]

#     filt1 = tabela["Nome ponto de decisão"].isin(["Exec. Projeto", "Exec. Business Case"])
#     filt2 = tabela["Status ponto de decisão"].isin(["Planejamento Exec.", "Ag. Execução"])

#     cond1 = tabela["Dt. Plan início"] <= pd.to_datetime("2024-02-14")
#     cond2 = tabela["Data real de início"].isnull()
#     cond3 = tabela["Dt. Plan início"].isnull()
#     cond4 = tabela["Data real de início"].notnull()

#     # Criando a janela
#     janela = Tk()
#     janela.geometry("800x600")
#     janela.title("Exibição de Tabela")

#     # Criando a tabela
#     tabela_tk = Frame(janela)
#     tabela_tk.pack()

#     # Criando os cabeçalhos da tabela
#     for i, coluna in enumerate(colunas):
#         Label(tabela_tk, text=coluna, font=("Arial", 12)).grid(row=0, column=i)

#     # Preenchendo a tabela com os dados
#     for i in range(len(tabela)):
#         if filt1[i] & filt2[i]:
#             if cond1[i] & cond2[i]:
#                 # Projetos atrasados ainda não iniciados
#                 cor = "red"
#             elif cond3[i]:
#                 # Projetos sem data de início planejada
#                 cor = "green"
#             elif cond4[i]:
#                 # Projetos com status incorreto
#                 cor = "orange"

#             for j, coluna in enumerate(colunas):
#                 Label(tabela_tk, text=tabela[coluna].iloc[i], font=("Arial", 10), fg=cor).grid(row=i+1, column=j)

#     # Exibindo a janela
#     janela.mainloop()

# item2()

   
from tkinter import *

def item2():
    # Definindo as colunas que serão impressas
    colunas = ["ID", "Nome", "Responsável", "Nome ponto de decisão", "Status ponto de decisão", "Data real de início"]

    filt1 = tabela["Nome ponto de decisão"].isin(["Exec. Projeto", "Exec. Business Case"])
    filt2 = tabela["Status ponto de decisão"].isin(["Planejamento Exec.", "Ag. Execução"])

    cond1 = tabela["Dt. Plan início"] <= pd.to_datetime("2024-02-14")
    cond2 = tabela["Data real de início"].isnull()
    cond3 = tabela["Dt. Plan início"].isnull()
    cond4 = tabela["Data real de início"].notnull()

    # Criando a janela
    janela = Tk()
    janela.geometry("800x600")
    janela.title("Exibição de Tabela")

    # Criando a tabela
    tabela_tk = Frame(janela)
    tabela_tk.pack()

    # Criando os cabeçalhos da tabela
    for i, coluna in enumerate(colunas):
        Label(tabela_tk, text=coluna, font=("Arial", 12), borderwidth=1).grid(row=0, column=i)

    # Preenchendo a tabela com os dados
    for i in range(len(tabela)):
        if filt1[i] & filt2[i]:
            if cond1[i] & cond2[i]:
                # Projetos atrasados ainda não iniciados
                cor = "red"
            elif cond3[i]:
                # Projetos sem data de início planejada
                cor = "green"
            elif cond4[i]:
                # Projetos com status incorreto
                cor = "orange"

            for j, coluna in enumerate(colunas):
                Label(tabela_tk, text=tabela[coluna].iloc[i], font=("Arial", 10), fg=cor, borderwidth=1).grid(row=i+1, column=j)

    # Exibindo o grid da tabela
    for i in range(len(tabela) + 1):
        tabela_tk.grid_rowconfigure(i, weight=1)
    for j in range(len(colunas)):
        tabela_tk.grid_columnconfigure(j, weight=1)

    # Exibindo a janela
    janela.mainloop()

item2()

   
# colunas = tabela.columns 
# print(colunas)

