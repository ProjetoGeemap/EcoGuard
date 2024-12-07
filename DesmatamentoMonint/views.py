from django.shortcuts import render
from .MapBiomas.querys import MapAlert as mp
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User

def get_image_links(request, item_id):
    # Suponha que você esteja buscando os links das imagens de algum banco de dados
    # ou gerando os links de alguma outra maneira.

    # Exemplo: gerando URLs baseados no ID do item (você pode substituir com sua lógica)
    before_image_url,after_image_url = mp.AnaliseCodigosAlertasDeflorationBahia(item_id)
    print(after_image_url)
    
    # Retornar os links em formato JSON
    return JsonResponse({
        'beforeImage': before_image_url,
        'afterImage': after_image_url
    })


def ListaDeAlertas(request):
    teste = str(request.user)
    print(teste)
    userALLBD = User.objects.filter(username=teste).first()
    
    if userALLBD:
        colection,codigos_alerta = mp.AlertasBahiaDefloration()
        colection = sorted(colection, key=mp.parse_date,reverse=True)
        return render(request,'desmatamento.html',{'colection':colection,'tamanho':len(colection)})
        
    elif teste !="AnonymousUser":
        colection,codigos_alerta = mp.AlertasBahiaDefloration()
        colection = sorted(colection, key=mp.parse_date,reverse=True)
        return render(request,'desmatamento.html',{'colection':colection,'tamanho':len(colection)})
    else:
        return HttpResponse("Voce precisa se logar")



