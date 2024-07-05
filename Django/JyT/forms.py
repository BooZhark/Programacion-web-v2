from django import forms
from .models import Usuario

from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'email','password', 'direccion']

