from django.shortcuts import render
from django.contrib.auth.models import User
from FireRadar.MapaBack import index
from .data_init import terra_brasilis
from django.http import HttpResponse

def GenerateOfMapa(request):
    teste = str(request.user)
    userALLBD = User.objects.filter(username=str(request.user)).first()
    if userALLBD :
            mapa = index.Initialization()
            Mapa_Container = mapa._repr_html_()
            fig = terra_brasilis.DadosExtract()
            dados = terra_brasilis.Dados_Year()
            return render(request,'fire_radar.html',locals())
    elif teste !="AnonymousUser":
        if request.user.is_autenticated:
            mapa = index.Initialization()
            Mapa_Container = mapa._repr_html_()
            fig = terra_brasilis.DadosExtract()
            dados = terra_brasilis.Dados_Year()
            return render(request,'fire_radar.html',locals())
    else:
         return render(request,'pasta_erro_page/not_login.html',locals())

def Previsao(request):
    teste = str(request.user)
    userALLBD = User.objects.filter(username=str(request.user)).first()
    if userALLBD:

        mapa,dadosDF = index.Previsoes()
        print(dadosDF)
        cont = mapa._repr_html_()
        dados =  dadosDF.to_dict('records')
        return render(request,'previsoes_incendios/previsao.html',locals())
    elif teste !="AnonymousUser":
        if request.user.is_autenticated:
            mapa,dadosDF = index.Previsoes()
            print(dadosDF)
            cont = mapa._repr_html_()
            dados =  dadosDF.to_dict('records')
            return render(request,'previsoes_incendios/previsao.html',locals())
    else:
         return render(request,'pasta_erro_page/not_login.html',locals())

