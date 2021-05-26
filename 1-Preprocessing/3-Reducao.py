import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def main():
    # Faz a leitura do arquivo
    input_file = '0.1-Output/2-dados_normalizados.csv'
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

    # PCA projection
    pca = PCA()
    principalComponents = pca.fit_transform(x)
    print("Explained variance per component:")
    print(pca.explained_variance_ratio_.tolist())
    print("\n\n")

    principalDf = pd.DataFrame(data=principalComponents[:, 0:2],columns=['principal component 1','principal component 2'])
    finalDf = pd.concat([principalDf, df[[target]]], axis=1)
    finalDf.to_csv('0.1-Output/3-dados_reduzidos.csv', index=False)
    ShowInformationDataFrame(finalDf, "Dataframe PCA")
    VisualizePcaProjection(finalDf, target)


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")


def VisualizePcaProjection(finalDf, targetColumn):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('2 component PCA', fontsize=20)
    targets = [0, 1, ]
    colors = ['r', 'g']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],finalDf.loc[indicesToKeep, 'principal component 2'],c=color, s=50)
    ax.legend(targets)
    ax.grid()
    plt.show()
    

if __name__ == "__main__":
    main()
