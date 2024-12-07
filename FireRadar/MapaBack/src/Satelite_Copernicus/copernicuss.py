import folium
from folium.plugins import Draw
from datetime import datetime, timedelta



def add_ee_layer(self, eeImageObject, visParams, name):
  import ee
  try:{
      ee.Initialize()
  }
  except:{
      ee.Authenticate()
  }

  tiles = ee.data.getTileUrl(eeImageObject.getMapId(visParams), 8014, 4817, 37)
  tiles = tiles[:-12] + "{z}/{x}/{y}"
  folium.raster_layers.TileLayer(
    tiles = tiles,
    attr = "Map Data © Google Earth Engine",
    name = name,
    overlay = True,
    control = True
  ).add_to(self)


def mask_s2_clouds(image):

  qa = image.select('QA60')

  # Bits 10 and 11 are clouds and cirrus, respectively.
  cloud_bit_mask = 1 << 10
  cirrus_bit_mask = 1 << 11

  # Both flags should be set to zero, indicating clear conditions.
  mask = (
      qa.bitwiseAnd(cloud_bit_mask)
      .eq(0)
      .And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
  )

  return image.updateMask(mask).divide(10000)


def Satelite_Copernicus():
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    data_10_dias_atras = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
    folium.Map.add_ee_layer = add_ee_layer


    dem = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED').filterDate  (data_10_dias_atras,data_hoje).filter(ee.Filter.lt ('CLOUDY_PIXEL_PERCENTAGE', 50)).map(mask_s2_clouds)

    visParams = {'min': 0.0,
        'max': 0.3,
        'bands': ['B4', 'B3', 'B2'],}


    myMap = folium.Map(location=[-12.1482,-44.9925], height=700)


    myMap.add_ee_layer(dem, visParams, 'Satelite COPERNICUS/S2')


    myMap.add_child(folium.LayerControl())
    draw = Draw()#adicionando menu de ferramentas
    draw.add_to(myMap)


    return myMap
