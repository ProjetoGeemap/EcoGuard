import requests
import re
import pandas as pd


def BrasilisExtractDados():
    # URL do diretório onde os arquivos estão listados
    print('verificando API Brasilis')
    url = 'https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/10min/'

    # Obter o conteúdo da página
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text

        # Encontrar todos os arquivos CSV na página
        files = re.findall(r'focos_10min_\d{8}_\d{4}\.csv', content)

        # Ordenar os arquivos e pegar o mais recente
        latest_file = sorted(files)[-1]

        # URL completa do arquivo mais recente
        latest_file_url = url + latest_file

        print(f'Último arquivo: {latest_file_url}')

        df = pd.read_csv(latest_file_url)
        df = df.rename(columns={'lat':'latitude','lon':'longitude'})    #renomeando colunas
        return df
    
    else:
        print('requisição vazia')
        return ''


