from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class registrarUsuarioForm(UserCreationForm):
      
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario',
                                                                'class': 'form-control',
                                                                }))  
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombres',
                                                                'class': 'form-control',
                                                                }))  
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellidos',
                                                                'class': 'form-control',
                                                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Correo',
                                                                'class': 'form-control',
                                                                }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
                                                                'class': 'form-control',
                                                                }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Reingrese Contraseña',
                                                                'class': 'form-control',
                                                                }))        
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = "Nombre de Usuario"
            self.fields['first_name'].label = "Nombres"
            self.fields['last_name'].label = "Apellidos"
            self.fields['email'].label = "Correo"
            self.fields['password1'].label = "Contraseña"
            self.fields['password2'].label = "Contraseña (Confirmación)"
            
    