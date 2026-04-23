from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    ROL_CHOICES = [
        ('mayor', 'Soy la persona mayor'),
        ('editor', 'Soy familiar de confianza (puedo gestionar todo)'),
        ('amigo', 'Soy familiar o amigo'),
    ]

    rol = forms.ChoiceField(
        choices=ROL_CHOICES,
        widget=forms.RadioSelect,
        label='¿Quién eres?'
    )
    nombre_grupo = forms.CharField(
        max_length=100,
        required=False,
        label='Nombre del grupo familiar (opcional)',
        help_text='Solo si eres el familiar de confianza que crea el grupo.'
    )
    first_name = forms.CharField(max_length=50, label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellidos', required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': (
                'Nombre de usuario (este nombre usarás para entrar en la app)'
            ),
        }
        help_texts = {
            'username': (
                'Elige un nombre fácil de recordar. '
                'Por ejemplo: maria, abuela, pepe.'
            ),
        }
