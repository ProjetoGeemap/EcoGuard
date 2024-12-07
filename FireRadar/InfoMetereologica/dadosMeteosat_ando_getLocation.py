from meteostat import Stations, Daily
from datetime import datetime
import pandas as pd
import requests
def get_location():
    response = requests.get('https://ipinfo.io/')
    data = response.json()
    usuario = data['loc']

    latitude = float(usuario[0:8])
    longitude = float(usuario[9:(len(usuario))])
    return latitude,longitude



def DadosMetereologicos(latitude,longitude):
    # Definir latitude e longitude
    Latitude = latitude
    Longitude = longitude

    # Encontrar a estação mais próxima para as coordenadas
    stations = Stations()
    station = stations.nearby(latitude, longitude).fetch(1)

    # Exibir a estação meteorológica encontrada
    #print(station)

    # Definir o intervalo de datas desejado
    
    start = datetime.now()
    start = start.strftime("%Y-%m-%d")
    end = datetime.now()
    end = end.strftime("%Y-%m-%d")

    # Coletar dados climáticos diários para a estação selecionada
    data = Daily(station, start,end)
    data = data.fetch()

    # Exibir os dados climáticos
    print(data)
    return pd.DataFrame(data)




#latitude,longitude = get_location()

#DadosMetereologicos(latitude,longitude)
