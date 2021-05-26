import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def main():
    # Faz a leitura do arquivo
    input_file = '0.1-Output/1-dados_limpos.csv'
    df = pd.read_csv(input_file)
    columns = list(df.columns)
    target = 'Class/ASD'
    index = -1
    for i, column in enumerate(columns):
        if column == target:
            index = i
            break
    del(columns[index])

    # Separating out the columns
    x = df.loc[:, columns].values
    # Separating out the target
    y = df.loc[:, [target]].values

    # Z-score normalization
    x_zcore = StandardScaler().fit_transform(x)
    normalized1Df = pd.DataFrame(data=x_zcore, columns=columns)
    normalized1Df = pd.concat([normalized1Df, df[[target]]], axis=1)
    ShowInformationDataFrame(normalized1Df, "Dataframe Z-Score Normalized")
    
    normalized1Df.to_csv('0.1-Output/2-dados_normalizados.csv', index=False)

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(15))
    print("\n")

if __name__ == "__main__":
    main()
