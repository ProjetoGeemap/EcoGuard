from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def PaginaPrincipalLP(request):
    return render(request,'index.html',locals())


def Login(request):
    if request.method == 'GET':
        return render (request,'login/login.html',locals())
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username = username, password=password)
        if user:
            login(request,user)
            
            return render(request,'first_page_after_login/inicio.html',locals())
        else:
            return render (request,'login/login.html',locals())
    


def Page_Init(request):
   
    teste = str(request.user)
    userALLBD = User.objects.filter(username=str(request.user)).first()
    if userALLBD :
         return render(request,'first_page_after_login/inicio.html',locals())
    elif teste !="AnonymousUser":
        if request.user.is_autenticated:
            return render(request,'first_page_after_login/inicio.html',locals())
    else:
         return render(request,'pasta_erro_page/not_login.html',locals())


def Page_Quem_Somos(request):
    return render(request,'quem_somos/quem_somos.html',locals())

def Cadastro(request):
    
    if request.method == "GET":
        return render(request,'cadastro/cadastro.html')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        userALLBD = User.objects.filter(username=username).first()
        emailALLBD = User.objects.filter(email=email).first()
        if userALLBD:
            return HttpResponse("Ja temos um usuario com esse USERNAME cadastrado")
            
        if emailALLBD:
            return HttpResponse("Ja temos um usuario com esse EMAIL cadastrado")
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return render (request,'login/login.html',locals())
    
    
    
def Not_Login(request):
    return render(request,'pasta_erro_page/not_login.html',locals())