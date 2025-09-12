# importações
import os

# funções
def area_quadrado(l):
    a = l**2
    return a

def area_retangulo(b, h):
    a = b*h
    return a

def area_triangulo(b, h):
    a = (b*h)/2
    return a

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")