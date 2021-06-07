from django.urls import path, include
from . import views
from .views import registrarUsuario, listarUsuario
from django.contrib.auth.views import login_required  

urlpatterns = [
    path('registrar',registrarUsuario.as_view(), name="registrar_usuario"),
    path('listar', login_required(listarUsuario.as_view()), name="listar_usuario"),
]


