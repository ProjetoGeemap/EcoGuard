import folium
import pandas as pd
import requests
from folium.plugins import MousePosition
from shapely.geometry import shape, Point
from folium.features import CustomIcon
from folium.plugins import Draw
from folium.plugins import LocateControl


def CreateFolium():
    geojasonFileLimites = 'https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-29-mun.json'

    response = requests.get(geojasonFileLimites)
    geojson_data = response.json()

    mapa = folium.Map([-12.42406, -41.68049], zoom_start=7,tiles="Cartodb Positron",height="100%")
    
    folium.TileLayer( tiles='http://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', attr='Google', name='Google Satellite', overlay=True, control=True ).add_to(mapa)
    folium.TileLayer( tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', attr='CartoDB Positron', name='CartoDB Positron', overlay=True, control=True ).add_to(mapa)
    LocateControl(strings={"title": "Localização Exata do Usuario", "popup": "Você está aqui :)"}).add_to(mapa)
    linhasBlack = lambda x: {"color": "black", 'fillOpacity': 0, 'weight': 0.3}
    folium.GeoJson(
        geojson_data,
        style_function=linhasBlack,
        tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['Cidade:'])
    ,name='Divisão Territorial').add_to(mapa)
    draw = Draw()#adicionando menu de ferramentas
    draw.add_to(mapa)

    folium.LayerControl().add_to(mapa)

    
    return mapa

def add_popup(feature):
    return folium.Popup(feature['properties']['name'])


def CreateOfMapa(df):

    geojasonFileLimites = 'https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-29-mun.json'

    response = requests.get(geojasonFileLimites)
    geojson_data = response.json()
    mapa = CreateFolium()
    # Filtragem Atenuadaaa dos pontos do DataFrame que estão dentro dos polígonos do GeoJSON
    for i, row in df.iterrows():
        point = Point(row['longitude'], row['latitude'])
        for feature in geojson_data['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                if (float(row['confidence']) >= 50)and (float(row['confidence']) <= 60):
                    marker_color = 'orange'
                    icon_color = 'red'
                elif (float(row['confidence']) > 60)and (float(row['confidence']) <= 68):
                    marker_color = 'red'
                    icon_color = 'yellow'
                    
                    
                elif (float(row['confidence']) > 68):
                    marker_color = 'darkred'
                    icon_color = 'yellow'
                else:
                    marker_color = 'lightgreen'
                    icon_color = 'gray'
            
                
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup='Latitude:'+ str(+row['latitude']) + " " + 'Longitude:'+str(row['longitude']) + " " + 'Satelite:'+str(row['satelite'])+" "+'Precisão:'+str(row['confidence'])+"%"
                ,icon=folium.Icon(color=marker_color,icon='glyphicon glyphicon-fire',icon_color=icon_color, prefix='glyphicon')).add_to(mapa)
                break
     
    return mapa