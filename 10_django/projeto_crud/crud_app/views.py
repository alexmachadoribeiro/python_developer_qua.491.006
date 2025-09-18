from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas":pessoas})