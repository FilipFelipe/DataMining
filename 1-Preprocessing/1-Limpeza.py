import re
import pandas as pd
import numpy as np

def tratar_arquivo():
    meuArquivo = open('0-Datasets/Autism-Child-Data.arff')
    arquivo = open("0-Datasets/Autism-Child-Data_Trabalhado.arff", "w")
    dados = meuArquivo.readlines()
    dado_tratado = list()
    for dado_linha in dados:
            if dado_linha[0] != "@":
                # NO = 0 | YES = 1 
                dado_linha = re.sub("no,", "0,", dado_linha)
                dado_linha = re.sub("yes,", "1,", dado_linha)
                dado_linha = re.sub(",NO", ",0", dado_linha)
                dado_linha = re.sub(",YES", ",1", dado_linha)
                # f = 0 | m = 1
                dado_linha = re.sub(",f", ",0", dado_linha)
                dado_linha = re.sub(",m", ",1", dado_linha)
                #relation {Parent - 0 | Self - 1 | Relative - 2 | 'Health care professional' - 3 | self - 4}
                dado_linha = re.sub("Parent,", "0,", dado_linha)
                dado_linha = re.sub("Self,", "1,", dado_linha)
                dado_linha = re.sub("self,", "1,", dado_linha)
                dado_linha = re.sub("Relative,", "2,", dado_linha)
                dado_linha = re.sub("'Health care professional',", "3,", dado_linha)
                dado_linha = re.sub("\s+", "", dado_linha)
                dado_tratado.append(dado_linha+"\n")
            else:
                print("Pulando linha")

    arquivo.writelines(dado_tratado)

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/Autism-Child-Data_Trabalhado.arff'
    df = pd.read_csv(input_file, names = ['A1_Score','A2_Score','A3_Score','A4_Score','A5_Score','A6_Score','A7_Score','A8_Score','A9_Score','A10_Score','age numeric','gender','ethnicity','jundice','austim','contry_of_res','used_app_before','result','age_desc','relation','Class/ASD'],usecols = ['age numeric','gender','austim','used_app_before','result','relation','Class/ASD'],na_values='?') 
    # Imprime as 15 primeiras linhas do arquivo
    
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(30))
    print("\n")

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")

    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")

    mean_Age = df['age numeric'].mean()
    df['age numeric'].fillna(round(mean_Age, 0), inplace=True)  
    mode_Relation = df['relation'].mode()[0]
    df['relation'].fillna(round(mode_Relation, 0), inplace=True)  
    # Imprime uma analise descritiva sobre dos dados
    print(df.info())
    print("\n")
    # Gera um arquivo csv com os todos os dados preenchidos pelo algoritmo
    df.to_csv('0.1-Output/1-dados_limpos.csv', index=False)
    print("\n")

if __name__ == "__main__":
    tratar_arquivo()
    main()


