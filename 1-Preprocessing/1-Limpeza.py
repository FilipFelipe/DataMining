import re
import pandas as pd
import numpy as np

def tratar_arquivo():
    meuArquivo = open('0-Datasets/StoneFlakes.dat')
    arquivo = open("0-Datasets/StoneFlakes_Trabalhado.dat", "w")
    dados = meuArquivo.readlines()
    dado_tratado = list()
    dados.remove('ID    LBI   RTI  WDI FLA  PSF  FSF ZDF1 PROZD\n')
    for dado_linha in dados:
        dado_linha = re.sub("\s+", ",", dado_linha,1)
        dado_linha = re.sub("\s+", "", dado_linha)
        dado_tratado.append(dado_linha+"\n")
    arquivo.writelines(dado_tratado)

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/StoneFlakes_Trabalhado.dat'
    df = pd.read_csv(input_file, names = ['ID','LBI','RTI','WDI','FLA','PSF','FSF','ZDF1','PROZD'],usecols = ['LBI','WDI','FLA','PSF','FSF','ZDF1','PROZD'],na_values='?') 
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
    mean_LBI = df['LBI'].mean()
    df['LBI'].fillna(mean_LBI, inplace=True)  
    mean_FLA = df['FLA'].mean()
    df['FLA'].fillna(mean_FLA, inplace=True)  
    mode_PSF = df['PSF'].mode()[0]
    df['PSF'].fillna(mode_PSF, inplace=True)    
    mode_FSF = df['FSF'].mode()[0]
    df['FSF'].fillna(mode_FSF, inplace=True)    
    mode_ZDF1 = df['ZDF1'].mode()[0]
    df['ZDF1'].fillna(mode_ZDF1, inplace=True)      
    
    # Gera um arquivo csv com os todos os dados preenchidos pelo algoritmo
    df.to_csv('2-Output/1-dados_limpos.csv', index=False)

if __name__ == "__main__":
    tratar_arquivo()
    main()


