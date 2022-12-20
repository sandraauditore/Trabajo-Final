
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication_app.forms import  UserRegisterForm


# Create your views here.

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST) 
        
        if formulario.is_valid():
            data = formulario.changed_data
        
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("store-inicio")
            else:
                return render(request, "authentication_app/login.html", {'form': formulario, 'errors': 'Credenciales invalidas'})    
        else:
            return render(request, "authentication_app/login.html", {'form': formulario, 'errors': formulario.errors})    

    formulario = AuthenticationForm()
    return render(request, "authentication_app/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):
    
    if request.method == "POST":      
        formulario=UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save
            return redirect("store-inicio")
        else:
            return render(request, "authentication_app/register.html", {'form': formulario, "errors": formulario.errors})
            
    formulario=UserRegisterForm()
    return render(request, 'authentication_app/register.html', {'form': formulario})
 
   
    
