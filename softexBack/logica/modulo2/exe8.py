import pandas as pd
import numpy

data = pd.read_csv("notas_alunos.csv")
 
def resultadoFinal(dataframe):

    media = (dataframe["nota_1"] + dataframe["nota_2"]) / 2
    dataframe = dataframe.assign(media = media)
    dataframe["situacao"] = " "

    dataframe.loc[(dataframe["media"] < 7) | (dataframe["faltas"] > 5),"situacao"] = "REPROVADO!"
    dataframe.loc[(dataframe["media"] >= 7) & (dataframe["faltas"] < 5),"situacao"] = "APROVADO!"

    print(dataframe)
    maiorFalta = dataframe["faltas"].max()
    maiorMedia =dataframe["media"].max()
    mediatotal = [10, 9, 8, 7, 6]

    print("A média geral das notas da turma é: ",numpy.mean(mediatotal))
    print("A maior quantidade de faltas é: ", maiorFalta)
    print("A maior média foi: ", maiorMedia)
    
resultadoFinal(data)