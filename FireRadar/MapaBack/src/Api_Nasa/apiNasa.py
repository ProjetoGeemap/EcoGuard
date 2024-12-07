import requests
from datetime import date
import pandas as pd
import io


import time
def InitDados():
    print('verificando API Nasa')
    MAP_KEY = '74907582915349f79637da6fc8860245' # key API -> decodificar depois
    SATELITE = 'VIIRS_NOAA20_NRT' #satelite fogo
    COUNTRY_CODE = 'BRA'
    DAY_RANGE = 2 #intervalo de dias range (data de hoje - dayRange) = ...,...,...,etc

    #URL filtragem por pais -> Nasa Firms
    #data_hoje = '2024-08-30'
    data_hoje = date.today()
    print(data_hoje)
    
    
    SateliteViirs = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{MAP_KEY}/{SATELITE}/{COUNTRY_CODE}/{DAY_RANGE}/" 
    SATELITE = 'MODIS_NRT' #TROCANDO DE SATELITE
    SateliteModis = f'https://firms.modaps.eosdis.nasa.gov/api/country/csv/{MAP_KEY}/{SATELITE}/{COUNTRY_CODE}/1'
    
    
    # Parâmetros da API
    
    parametros = {
        "country":"BRA",  # Código do país para o Brasil
        "mapKey": "74907582915349f79637da6fc8860245"  # MAP_KEY nasa. Patrick lembrar de ver depois o status  
    }
    
    # DOIS SATELITES
    escolhendoSatelite = '1'
    if escolhendoSatelite == '1':
        response = requests.get(SateliteModis, params=parametros)
        if response.status_code == 200:#solicitação foi bem-sucedida
            print('Code 200 http ')
            df = pd.read_csv(io.StringIO(response.text))  #convertendo minha response em um DataFrame
            df = df.rename(columns={'instrument':'satelite'})
            return df
        else: #solicitação não foi bem-sucedida   
            print(f"Erro ao obter dados: {response.status_code}")
     
        
    if escolhendoSatelite == '2':
        response = requests.get(SateliteViirs, params=parametros)#reuisição satelite VIIRS
        if response.status_code == 200:#solicitação foi bem-sucedida

            print('Code 200 http ')
            df = pd.read_csv(io.StringIO(response.text))  #convertendo minha response em um DataFrame
            df = df.rename(columns={'instrument':'satelite'})
            return df
    
       
        else: #solicitação não foi bem-sucedida   
            print(f"Erro ao obter dados: {response.status_code}")
    
    
    
        


#Tratar Dados DataFrame
#DfBahia = tratamento.TratamentoViirs(InitDados()) #-> tratando dados VIIRS
#DfBahia = tratamento.TratamentoModis(InitDados()) #-> tratando dados Modis




#Montar Mapa foliu com esses dados tratados
#mapa.CreateOfMapa(DfBahia)




#criar um dashboard ou algo para ver informações

#Pensar em metodologia com Keras para modelos de previsões
    