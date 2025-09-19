from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas":pessoas})

def cadastro_pessoa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        Pessoa.objects.create(nome=nome, email=email, cpf=cpf)
        return redirect('home')
    return render(request, 'cadastrar.html')