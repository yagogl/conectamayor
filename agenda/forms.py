from django import forms
from .models import Recordatorio


class RecordatorioMayorForm(forms.ModelForm):
    """Formulario simplificado: solo 3 campos con iconos grandes."""
    TIPO_CHOICES_ICONOS = [
        ('pastilla', '💊 Pastilla'),
        ('medico', '🏥 Médico'),
        ('llamada', '📞 Llamada'),
        ('cumple', '🎂 Cumpleaños'),
        ('otro', '📌 Otro'),
    ]

    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES_ICONOS,
        widget=forms.RadioSelect,
        label='Tipo'
    )

    class Meta:
        model = Recordatorio
        fields = ['titulo', 'tipo', 'fecha']
        labels = {
            'titulo': '¿Qué tienes que hacer?',
            'fecha': '¿Cuándo?',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class RecordatorioEditorForm(forms.ModelForm):
    """Formulario completo para el familiar-editor."""
    class Meta:
        model = Recordatorio
        fields = ['titulo', 'tipo', 'fecha', 'hora']
        labels = {
            'titulo': 'Título',
            'tipo': 'Tipo',
            'fecha': 'Fecha',
            'hora': 'Hora (opcional)',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
