from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

app_name = 'agenda'

@login_required
def lista(request):
    return render(request, 'proximamente.html', {'modulo': 'Agenda'})

urlpatterns = [
    path('', lista, name='lista'),
]
