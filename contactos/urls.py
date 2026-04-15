from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

app_name = 'contactos'

@login_required
def lista(request):
    return render(request, 'proximamente.html', {'modulo': 'Contactos'})

urlpatterns = [
    path('', lista, name='lista'),
]
