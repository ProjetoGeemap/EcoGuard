import xarray as xr
import tempfile
import folium
import requests
import re
import numpy as np
from folium.plugins import Draw, LocateControl,MeasureControl


def CreateFolium():
    geojasonFileLimites = 'https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-29-mun.json'
    response = requests.get(geojasonFileLimites)
    geojson_data = response.json()

    mapa = folium.Map([-12.42406, -41.68049], zoom_start=7, tiles="Cartodb Positron", height="100%",control_scale=True,zoom_control=True)
    LocateControl(strings={"title": "Localização Exata do Usuario", "popup": "Você está aqui :)"}).add_to(mapa)
    linhasBlack = lambda x: {"color": "black", 'fillOpacity': 0, 'weight': 0.3}
    folium.GeoJson(
        geojson_data,
        style_function=linhasBlack,
        tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['Cidade:'])
    ).add_to(mapa)
    draw = Draw()  # Adicionando menu de ferramentas
    draw.add_to(mapa)
    return mapa



def List():
    url='https://dataserver-coids.inpe.br/queimadas/queimadas/riscofogo_meteorologia/observado/risco_fogo/'
    response = requests.get(url=url)
    if response.status_code == 200:
        content = response.text

        # Encontrar todos os arquivos CSV na página
        files = re.findall(r'INPE_FireRiskModel_2.2_FireRisk_\d{8}.nc', content)
        # Ordenar os arquivos e pegar o mais recente
        latest_file = sorted(files)[-1]

        # URL completa do arquivo mais recente
        latest_file_url = url + latest_file
     
        response = requests.get(latest_file_url)
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(response.content)
            tmp_file_path = tmp_file.name

            return tmp_file_path

def Previsao_incendio_hoje():
    # Carrega o arquivo NetCDF
    ds = xr.open_dataset(List())
    df = ds.to_dataframe().reset_index()
    # Exibir uma visão geral do dataset



    lat_min, lat_max = -17.5, -9.6
    lon_min, lon_max = -46.5, -39.0


    df_filtered = df[(df['lat'] >= lat_min) & (df['lat'] <= lat_max) &
                           (df['lon'] >= lon_min) & (df['lon'] <= lon_max) & (df['rf']>=1.00)]


    df_filtered.loc[:, 'lat'] = df_filtered['lat'].round(3)
    df_filtered.loc[:, 'lon'] = df_filtered['lon'].round(3)
    df_filtered.drop_duplicates(subset=['lat','lon'])

    df_clean = df_filtered.drop_duplicates(subset=['lat', 'lon'])

    print(df_clean)

    df_sampled = df_clean.sample(frac=0.00029, random_state=42)
    print("DF ALEATORIO")
    print(df_sampled)
   # mapa = folium.Map([-12.42406, -41.68049], zoom_start=7,tiles="Cartodb   Positron",height=600)
    mapa = CreateFolium()

    for _, row in df_sampled.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=5,  # Tamanho do marcador
            color='red',  # Cor do círculo
            fill=True,
            fill_color='red',
            fill_opacity=0.6,
            popup=f"Lat: {row['lat']}, Lon: {row['lon']}"  # Informação exibida     ao clicar
        ).add_to(mapa)

    return mapa,df_sampled
    
    