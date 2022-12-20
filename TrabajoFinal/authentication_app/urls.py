from django.urls import path
from authentication_app.views import * 





urlpatterns = [
    path("login", iniciar_sesion, name="auth-login"),
    path("register", registrar_usuario, name="auth-register")
     
]
