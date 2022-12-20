from django.urls import path
from store.views import *

urlpatterns = [
    path("inicio", inicio, name="store-inicio"),
    path("galeria", GaleriaCreateView.as_view(), name="store-galeria"),
    path("galeria/list", GaleriaListView.as_view(), name="store-galeria-listado"),
    path("contacto", creacion_Contacto, name="store-contacto"), 
    path("about", about, name="store-about"),
]


