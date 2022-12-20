
from urllib import request
from store.forms import  ContactoFormulario
from store.models import Galeria, Contacto
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

# Create your views here.

def inicio(request):
    return render(request, "store/index.html")

#def creacion_Galeria(request):
    #if request.method == "POST":
        #formulario=GaleriaFormulario(request.POST)
        #if formulario.is_valid():
           #data  = formulario.cleaned_data
           #galeria = Galeria(Nombre=data['Nombre'], Descripcion=data['Descripcion'], Imagen=data['Imagen'], Precio=data['Precio'] )
           #galeria.save()
    #formulario = GaleriaFormulario()  
    #return render(request, 'store/galeria.html', {'formulario': formulario})   


def creacion_Contacto(request):

    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            contacto = Contacto(Nombre=data["Nombre"], Email=data["Email"], Mensaje=data["Mensaje"])
            contacto.save()
    formulario = ContactoFormulario()
    return render(request, "store/contacto.html", {"formulario": formulario})

class GaleriaCreateView(CreateView):
    model = Galeria
    fields = "__all__" 
    template_name = "store/galeria.html"
    success_url = "/store/galeria"

class GaleriaListView(ListView):
    model = Galeria
    template_name = "store/galeria.html"



def about(request):
    return render(request, "store/about.html") 
    

