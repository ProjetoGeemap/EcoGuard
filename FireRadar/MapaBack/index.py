from .src.Api_Nasa import apiNasa
from .src.MapaConstruct import  mapa as mapa
from .src.TratamentoDataFrame import tratamento as tratamento
from .src.Api_Brasilis import apiBrasilis
from .src.Satelite_Copernicus import copernicuss as copernicus
from .src.Focos_previstos_today import focos_previstos_hoje 

import pandas as pd
import folium
def Initialization():
    #dadoss_brasilis = apiBrasilis.BrasilisExtractDados()
    #BrasilisTratado = tratamento.TratamentoBrasilis(dadoss_brasilis)
    dados_modis = apiNasa.InitDados()
    MODISTratado = tratamento.TratamentoModis(dados_modis)
    #juntandoDatasFrames = pd.concat([BrasilisTratado,MODISTratado])
    #print(juntandoDatasFrames)

    #mapa.CreateOfMapa(juntandoDatasFrames)
    
    return mapa.CreateOfMapa(MODISTratado)


def Previsoes():
    mapa,df_dados = focos_previstos_hoje.Previsao_incendio_hoje()
    return mapa,df_dados