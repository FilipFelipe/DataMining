import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/echocardiogram.data'
    print(input_file)
    df = pd.read_csv(input_file, names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening','epss','lvdd','wall-motion-score','wall-motion-index','mult','name','group','alive-at-1'],usecols = ['survival','still-alive','age-at-heart-attack','alive-at-1'],na_values='?') 
    # Imprime as 15 primeiras linhas do arquivo
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")

    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")
    mean_LBI = df['survival'].mode()[0]
    df['survival'].fillna(mean_LBI, inplace=True)  
    mean_FLA = df['still-alive'].mode()[0]
    df['still-alive'].fillna(mean_FLA, inplace=True)  
    mode_PSF = df['age-at-heart-attack'].mean()
    df['age-at-heart-attack'].fillna(mode_PSF, inplace=True)    
    print(df.info())
    # Gera um arquivo csv com os todos os dados preenchidos pelo algoritmo
    df.to_csv('2-Output/1-dados_echocardiogram.csv', index=False)

    idade= df['age-at-heart-attack']
    tamanho= len(idade)
    cl = int(round(tamanho**(1/2),0))
    plt.title("Histograma de Idades")
    plt.xlabel("Idades")
    plt.ylabel("Frequências")
    plt.hist(idade, bins = cl, range = ( min(idade), max(idade)), alpha = 0.6, color = 'r')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()


