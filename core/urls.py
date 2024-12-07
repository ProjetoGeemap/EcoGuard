
from django.contrib import admin
from django.urls import path,include
from FireRadar import views
from core import views as views2
from DesmatamentoMonint import views as dematamentoViews

from DesmatamentoMonint import views as desmatamento

urlpatterns = [
    path('admin/', admin.site.urls),

    #ferramenta Fire Radar
    path('fire_radar/',views.GenerateOfMapa,name="Ferramenta_Fire_Radar"),
    path('fire_radar/previsao',views.Previsao,name="Ferramenta_Previsao"),
    
    #paginas index,inicio, login, qm somos
    path('',views2.PaginaPrincipalLP,name='home'),
    path('inicio/', views2.Page_Init),
    path('login/',views2.Login, name="login"),
    
    path('cadastro/',views2.Cadastro, name="cadastro"),
    path('quem_somos/',views2.Page_Quem_Somos, name="Quem_somos"),
    
    #ferramenta desmatamento
    path('desmatamento/',desmatamento.ListaDeAlertas,name='Ferramenta_Desmatamento'),
    path('get-image-links/<int:item_id>/', dematamentoViews.get_image_links, name='get_image_links'),
    
    path('not_login/',views2.Not_Login,name="not_login")
    #ferramenta CLima Tauan
    
    
]
