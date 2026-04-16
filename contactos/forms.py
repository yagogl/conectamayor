from django import forms
from .models import Contacto


class ContactoMayorForm(forms.ModelForm):
    """Formulario simplificado para el mayor."""
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'categoria']
        labels = {
            'nombre': '¿Cómo se llama?',
            'telefono': 'Teléfono',
            'categoria': 'Tipo de contacto',
        }


class ContactoEditorForm(forms.ModelForm):
    """Formulario completo para el familiar-editor."""
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'categoria', 'direccion', 'notas']
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
            'categoria': 'Categoría',
            'direccion': 'Dirección',
            'notas': 'Notas',
        }
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 2}),
            'notas': forms.Textarea(attrs={'rows': 2}),
        }
