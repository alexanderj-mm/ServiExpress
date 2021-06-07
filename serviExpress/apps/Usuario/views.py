from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import registrarUsuarioForm




# Create your views here.

class registrarUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar_usuario.html"
    form_class = registrarUsuarioForm
    success_url = reverse_lazy('index')
 
class listarUsuario(ListView):
    model = User
    template_name = 'Usuario/listar_usuario.html'
    
  

 
