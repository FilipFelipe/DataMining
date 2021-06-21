import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    input_file = '0.1-Output/1-dados_limpos.csv'  # Importação dos Dados
    df = pd.read_csv(input_file, usecols=[
                     'age numeric', 'result', 'gender', 'result', 'Class/ASD'])
    
    #histrograma de idades 
    idade = df['age numeric'].tolist()
    plt.title('Histograma de idade')
    plt.ylabel('Frequência')
    plt.hist(idade, 20, rwidth=0.9, edgecolor='black')
    plt.show()

    #Gráficos de idades 
    somas_idades = df['age numeric'].value_counts(sort=True)
    somas_idades.plot.pie(autopct='%1.1f%%',
                          startangle=90, title='Idade dos participantes',ylabel='')
    plt.show()

    #Gráficos de gênero
    somas_genero = df['gender'].value_counts(sort=True)
    somas_genero.plot.pie(labels=['Masculino', 'Feminino'], autopct='%1.1f%%',
                          startangle=90, title='Gênero dos participantes da pesquisa',ylabel='')
    plt.show()

    #Gráficos de Resultados
    somas_result = df['result'].value_counts(sort=True)
    somas_result.plot.pie(
        startangle=90, title='Resultados',ylabel='')
    plt.show()

    #Gráficos de classificacao
    somas_classificacao = df['Class/ASD'].value_counts(sort=True)
    somas_classificacao.plot.pie(labels=['Grau de Autismo', 'Sem Grau de Autismo'],autopct='%1.1f%%',
                          startangle=90, title='Classificação dos participantes',ylabel='')
    plt.show()

    df.to_csv('0.1-Output/1-dados_graficos.csv', index=False)

if __name__ == "__main__":
    main()
