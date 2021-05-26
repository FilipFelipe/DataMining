import re
import pandas as pd
import numpy as np


def main():
    # Faz a leitura do arquivo
    input_file = '0.1-Output/1-dados_limpos.csv'
    df = pd.read_csv(input_file) 
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")

    print("Moda dos dados\n")
    print(df.mode())
    print("\n")

    print("Mediana dos dados\n")
    print(df.median())
    print("\n")

    print("Média dos dados\n")
    print(df.mean())
    print("\n")

    print("Variancia dos dados\n")
    print(df.var())
    print("\n")

    print("Amplitude\n")
    print(df.max()-df.min())
    print("\n")

    print("Desvio Padrao\n")
    print(df.std())
    print("\n")

    print("Desvio Abs\n")
    print(df.mad())
    print("\n")

    print("Desvio Covariância e Correlação\n")
    print(df.cov())
    print(df.corr())
    print("\n")






if __name__ == "__main__":
    main()


