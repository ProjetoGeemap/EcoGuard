import pandas as pd


def TratamentoViirs(df):
    df[['latitude','longitude']] # filtrando colunas que quero
    latitude_min, latitude_max = -17.5, -8.0
    longitude_min, longitude_max = -46.5, -37.0
    df_bahia = df[(df['latitude'] >= latitude_min) & (df['latitude'] <= latitude_max) &
              (df['longitude'] >= longitude_min) & (df['longitude'] <= longitude_max)] #& ((df['confidence'] != 'l'))]
    #df = df.rename(columns={'satellite':'satelite'})
    print(f'quantidade encontrada : {len(df_bahia)}')

    return df_bahia

def TratamentoModis(df):
    df[['latitude','longitude']] # filtrando colunas que quero
    latitude_min, latitude_max = -17.5, -8.0
    longitude_min, longitude_max = -46.5, -37.0
    df_bahia = df[(df['latitude'] >= latitude_min) & (df['latitude'] <= latitude_max) &
              (df['longitude'] >= longitude_min) & (df['longitude'] <= longitude_max) & ((df['confidence'] >= 40))]
    df = df.rename(columns={'satellite':'satelite'})
    print(f'quantidade encontrada : {len(df_bahia)}')

    return df_bahia



def TratamentoBrasilis(df):
    df[['latitude','longitude']] # filtrando colunas que quero
    latitude_min, latitude_max = -17.5, -8.0
    longitude_min, longitude_max = -46.5, -37.0
    df_bahia = df[(df['latitude'] >= latitude_min) & (df['latitude'] <= latitude_max) &
              (df['longitude'] >= longitude_min) & (df['longitude'] <= longitude_max)]
    
    print(f'quantidade encontrada : {len(df_bahia)}')
    return df_bahia