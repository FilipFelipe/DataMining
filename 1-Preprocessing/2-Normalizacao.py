import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def main():
    # Faz a leitura do arquivo
    input_file = '2-Output/1-dados_limpos.csv'
    df = pd.read_csv(input_file)
    columns = list(df.columns)
    target = 'ZDF1'
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

    # Mix-Max normalization
    x_minmax = MinMaxScaler().fit_transform(x)
    normalized2Df = pd.DataFrame(data=x_minmax, columns=columns)
    normaizeld2Df = pd.concat([normalized2Df, df[[target]]], axis=1)
    ShowInformationDataFrame(normalized2Df, "Dataframe Min-Max Normalized")
    
    normalized2Df.to_csv('2-Output/2-dados_normalizados.csv', index=False)

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(15))
    print("\n")

if __name__ == "__main__":
    main()
