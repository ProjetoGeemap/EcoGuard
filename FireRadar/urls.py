from django.urls import path
from FireRadar import views


urlpatterns = [
    path('',views.GenerateOfMapa),
    path('dash/',views.Graphl),
    path('previsao',views.Previsao)
    
]