import requests as re
import pandas as pd

def DadosExtract():
    url ='https://terrabrasilis.dpi.inpe.br/queimadas/situacao-atual/media/estado/csv_estatisticas/historico_estado_bahia.csv'
    

    
    df = pd.read_csv(url)
    total = df.iloc[[27,28,29],:]
    df = df.drop(index=[27,28,29])
    df.rename(columns={'Unnamed: 0': 'Ano'}, inplace=True)

    # Criar o gráfico temporal


def TrateOfUrl(url):

    response = re.get(url)
    
        
    return response.text


def Dados_Year():
    url='https://terrabrasilis.dpi.inpe.br/queimadas/situacao-atual/media/estado/csv_estatisticas/historico_estado_bahia.csv'
    df = pd.read_csv(url)
    df.rename(columns={'Unnamed: 0': 'Ano'}, inplace=True)
    df.fillna("Nan", inplace=True)
    df2 = df.to_dict('records')
    return df2
    
    