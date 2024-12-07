import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta as delta


token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwMzQ1LCJuYW1lIjoiUHJvamV0byBHZWVtYXAiLCJlbWFpbCI6InByb2pldG9nZWVtYXBAZ21haWwuY29tIiwicHJvZmlsZSI6InJlZ3VsYXIiLCJhdmF0YXIiOm51bGwsImxhc3RfbG9naW5fYXQiOiIyMDI0LTA5LTIxIDE3OjQzOjQzIC0wMzAwIiwibGFzdF91cGRhdGVkX3Bhc3N3b3JkX2F0IjoiMjAyNC0wOS0yMSAxNzowMToxMiAtMDMwMCIsIm5vdGlmeV91c2VyX25ld190ZXJtX29mX3VzZV92ZXJzaW9uIjpmYWxzZSwidW5zZWVuX2FsZXJ0cyI6MCwiaW5zdGl0dXRpb24iOnsiaWQiOm51bGwsIm5hbWUiOm51bGwsImFiYnJldmlhdGlvbiI6bnVsbH0sImV4cCI6MTcyNjk3MTUwOH0.Pq3ucnzCjTPBGi8nGHziEwvVKAA15jVw4NDtNNVO7Xk'

# Define o URL da API
url = 'https://plataforma.alerta.mapbiomas.org/client/v2/graphql'


def AlertasBahiaDefloration():
# Cabeçalhos da requisição
  header = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}


  DateEnd = datetime.today()
  DateStart = DateEnd-delta(months=4)
  DateEnd = str(DateEnd.strftime("%Y-%m-%d"))
  DateStart = str(DateStart.strftime("%Y-%m-%d"))

  query = """
  query GetPublishedAlertsNew($alertCodes: [ID!] = [], $propertyCodes:  [ID!] = [], $page: Int = 1, $limit: Int = 200, $startDate: BaseDate,   $endDate: BaseDate, $dateType: DateTypes!, $startSize: Float = 0.0,   $endSize: Float = 9999999.0, $territoryIds: [Int!] = [],  $territoryCategory: String, $sources: [SourceTypes!],  $intersectWithCar: Boolean, $isInEmbargoedArea: Boolean,   $isInAuthorizedArea: Boolean, $deforestationClasses:  [DeforestationTypes!] = [All], $actionTypesIds: [Int!] = [],   $boundingBox: [Float!], $sortField: AlertSortField, $sortDirection:   SortDirection) {
    alerts(
      alertCodes: $alertCodes
      propertyCodes: $propertyCodes
      page: $page
      limit: $limit
      startDate: $startDate
      endDate: $endDate
      dateType: $dateType
      startSize: $startSize
      endSize: $endSize
      territoryIds: $territoryIds
      territoryCategory: $territoryCategory
      sources: $sources
      intersectWithCar: $intersectWithCar
      isInEmbargoedArea: $isInEmbargoedArea
      isInAuthorizedArea: $isInAuthorizedArea
      deforestationClasses: $deforestationClasses
      actionTypesIds: $actionTypesIds
      boundingBox: $boundingBox
      sortField: $sortField
      sortDirection: $sortDirection
    ) {
      metadata {
        currentPage
        limitValue
        totalCount
        totalPages
        __typename
      }
      collection {
        alertCode
        areaHa
        detectedAt
        alertGeometry {
          code
          __typename
        }
        crossedBiomes
        crossedCities
        crossedStates
        crossedRuralProperties {
          id
          code
          areaHa
          alertAreaInCar
          type
          __typename
        }
        __typename
      }
      __typename
    }
  }

  """

  variables = {
    "alertCodes": [],
    "propertyCodes": [],
    "page": 1,
    "limit": 500,
    "startSize": 0,
    "endSize": 9999999,
    "territoryIds": [
      18398
    ],
    "deforestationClasses": [
      "All"
    ],
    "actionTypesIds": [],
    "startDate": DateStart,
    "endDate": DateEnd,
    "dateType": "DetectedAt",
    "sources": [
      "All"
    ],
    "sortField": "DETECTED_AT",
    "sortDirection": "DESC"
  }



  response = requests.post(url,headers=header,json={'query':query,  'variables':variables})


  data =response.json()
  data = data['data']['alerts']['collection']
  CODIGOS_ALERTA = []
  collections = []
  for i in range(len(data)):
    CODIGOS_ALERTA.append(data[i]['alertCode'])
    collections.append(data[i])
  return collections , CODIGOS_ALERTA
  

def AnaliseCodigosAlertasDeflorationBahia(alertaCode):
  header = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
 }

  query = """
  query alert($alertCode: Int!) {
    alert(alertCode: $alertCode) {
      areaHa
      detectedAt
      statusAt
      republished
      publishedAt
      alertCode
      alertGeometry {
        code
        __typename
      }
      actions {
        process
        actionType
        institutionName
        __typename
      }
      crossedBiomes
      crossedStates
      crossedCities
      crossedQuilombos
      crossedQuilombosArea
      crossedSettlements
      crossedSettlementsArea
      crossedSettlementsRuralPropertiesList
      crossedForestManagementsArea
      crossedForestManagementsCategories
      crossedBiosphereReserves
      crossedBiosphereReservesArea
      crossedDeforestationAuthorizationsArea
      crossedIndigenousLandsArea
      crossedIndigenousLands
      crossedGeoparks
      crossedGeoparksArea
      crossedSpecialTerritories
      crossedSpecialTerritoriesArea
      crossedSpecialTerritoriesIds
      crossedSpecialTerritoryAmacroArea
      crossedSpecialTerritoryAmazoniaLegalArea
      crossedSpecialTerritoryLeiDaMataAtlanticaArea
      crossedSpecialTerritoryMatopibaArea
      crossedSpecialTerritorySemiaridoArea
      crossedConservationUnits
      crossedConservationUnitsArea
      crossedRiverSourcesArea
      crossedEmbargoesRuralPropertiesTotal
      crossedEmbargoesRuralPropertiesArea
      crossedFederalProtectedAreaSustainableUses
      crossedFederalProtectedAreaSustainableUsesArea
      crossedFederalProtectedAreaIntegralProtections
      crossedFederalProtectedAreaIntegralProtectionsArea
      crossedStateProtectedAreaSustainableUses
      crossedStateProtectedAreaSustainableUsesArea
      crossedStateProtectedAreaIntegralProtections
      crossedStateProtectedAreaIntegralProtectionsArea
      crossedMunicipalityProtectedAreaSustainableUses
      crossedMunicipalityProtectedAreaSustainableUsesArea
      crossedMunicipalityProtectedAreaIntegralProtections
      crossedMunicipalityProtectedAreaIntegralProtectionsArea
      crossedRuralProperties {
        id
        code
        areaHa
        alertAreaInCar
        type
        version
        alertAreaInCar
        __typename
      }
      sources
      boundingBox {
        simplified
        __typename
      }
      publishedImages {
        reference
        acquiredAt
        url
        __typename
      }
      statusName
      __typename
    }
  }
  """
  variables = {
  "alertCode": alertaCode
}  
  
  response = requests.post(url,json={'query':query,'variables':variables},headers=header)
  
  data = response.json()
  antes = data['data']['alert']['publishedImages'][0]
  depois = data['data']['alert']['publishedImages'][1]

  print("Antes : ",antes['url'], "Data ",antes['acquiredAt'])
  print("Depois : ",depois['url'], "Data ",depois['acquiredAt'])
  return antes['url'],depois['url']

def MotorStart():
  listaCodigos = AlertasBahiaDefloration()
  for i in range(len(listaCodigos)):
    AnaliseCodigosAlertasDeflorationBahia(listaCodigos[i])



def parse_date(d_item):
    from datetime import datetime
    return datetime.strptime(d_item['detectedAt'], '%Y-%m-%d')

def LaudosAlert(alertCode):
  query = """query GetAlertReportNewData($alertCode: Int!, $carId: Int, $propertyCode: String) {
  alert(alertCode: $alertCode) {
    alertCode
    statusName
    statusAt
    republished
    ruralPropertiesCodes
    crossedBiomes
    crossedBiomesList
    crossedWatersheds
    crossedWatershedsList
    crossedStates
    crossedStatesList
    crossedCities
    crossedCitiesList
    deforestationClasses
    sources
    areaHa
    publishedAt
    detectedAt
    publishedImages(carId: $carId, carCode: $propertyCode) {
      url
      acquiredAt
      constellation
      reference
      satellite
      __typename
    }
    alertGeometry {
      imageGridMeasurements
      changes
      changesUsageAndCoverageSentinel
      changesLandsatMosaicRgb
      layerImage
      afterDeforestationSimplifiedImage
      simplifiedPoints {
        number
        xCoord
        yCoord
        __typename
      }
      __typename
    }
    boundingBox {
      neLat
      neLng
      swLat
      swLng
      __typename
    }
    ruralPropertiesTotal
    crossedQuilombos
    crossedQuilombosArea
    crossedQuilombosList
    crossedSettlements
    crossedSettlementsArea
    crossedSettlementsList
    crossedSettlementsRuralPropertiesList
    crossedSettlementsRuralPropertiesArea
    crossedForestManagementsArea
    crossedForestManagementsCategories
    crossedForestManagementsList
    crossedBiosphereReserves
    crossedBiosphereReservesArea
    crossedDeforestationAuthorizationsArea
    crossedDeforestationAuthorizationsList
    crossedDeforestationAuthorizationsCategories
    crossedDeforestationAuthorizationsActivities
    crossedDeforestationAuthorizationRuralPropertiesList
    crossedDeforestationAuthorizationRuralPropertiesArea
    crossedForestManagementRuralPropertiesList
    crossedForestManagementRuralPropertiesArea
    crossedIndigenousLandsArea
    crossedIndigenousLands
    crossedIndigenousLandsList
    crossedGeoparks
    crossedGeoparksArea
    crossedSpecialTerritories
    crossedSpecialTerritoriesArea
    crossedSpecialTerritoryAmacroArea
    crossedSpecialTerritoryAmazoniaLegalArea
    crossedSpecialTerritoryLeiDaMataAtlanticaArea
    crossedSpecialTerritoryMatopibaArea
    crossedSpecialTerritorySemiaridoArea
    crossedConservationUnits
    crossedConservationUnitsList
    crossedConservationUnitsArea
    crossedRiverSourcesArea
    crossedEmbargoesRuralPropertiesTotal
    crossedEmbargoesRuralPropertiesArea
    crossedEmbargoesRuralPropertiesList
    crossedFederalProtectedAreaSustainableUses
    crossedFederalProtectedAreaSustainableUsesArea
    crossedFederalProtectedAreaIntegralProtections
    crossedFederalProtectedAreaIntegralProtectionsArea
    crossedStateProtectedAreaSustainableUses
    crossedStateProtectedAreaSustainableUsesArea
    crossedStateProtectedAreaIntegralProtections
    crossedStateProtectedAreaIntegralProtectionsArea
    crossedMunicipalityProtectedAreaSustainableUses
    crossedMunicipalityProtectedAreaSustainableUsesArea
    crossedMunicipalityProtectedAreaIntegralProtections
    crossedMunicipalityProtectedAreaIntegralProtectionsArea
    classesLabels {
      name
      colors
      colorsWithLabels
      __typename
    }
    warnings {
      pt
      en
      __typename
    }
    crossedPermanentProtectedList
    crossedPermanentProtectedArea
    crossedLegalReservesList
    crossedLegalReservesArea
    crossedLegalReserveRuralPropertiesList
    crossedPermanentProtectedRuralPropertiesList
    crossedPermanentProtectedRuralPropertiesArea
    crossedRuralProperties {
      id
      code
      type
      alertAreaInCar
      alertInPropertyImage
      propertyInStateImage
      __typename
    }
    supportCases(carId: $carId, carCode: $propertyCode) {
      code
      supportCaseType
      subject
      description
      carId
      carCode
      alertCode
      authorizedAreaHa
      authorizingAgency
      expirationDate
      processNumber
      propertyName
      documentIssueDate
      supportCaseFiles {
        id
        name
        fileType
        fileUploadedUrl
        __typename
      }
      supportCaseStatus {
        observation
        supportCaseStatus
        createdAt
        __typename
      }
      supportCaseStatusCount
      __typename
    }
    actions {
      process
      actionType
      institutionName
      __typename
    }
    ruralProperties(carId: $carId, carCode: $propertyCode) {
      rAlertGeometriesRuralProperties {
        alertAreaInCar
        alertGeometry {
          relatedAlert {
            alertCode
            areaHa
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
  sources {
    portugueseName
    englishName
    portugueseType
    englishType
    portugueseCategory
    englishCategory
    updateDate
    updateSource
    key
    __typename
  }
  methodologies {
    portugueseContent
    englishContent
    indonesianContent
    url
    __typename
  }
}
"""


  variables = {
  "alertCode": alertCode,
  "carId": None
}
  header = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
  response = requests.post(url,headers=header,json={'query':query,  'variables':variables})


  data =response.json()
  print(data)
  
