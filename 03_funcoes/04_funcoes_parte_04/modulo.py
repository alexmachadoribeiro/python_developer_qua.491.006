# importa biblioteca
import os

# funções
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def velocidade_media(vi, vf):
    vm = vf-vi
    return vm

def tempo_medio(tf, ti):
    tm = tf-ti
    return tm

def aceleracao_media(vm, tm):
    am = vm/tm
    return am

def mru(si, v, t):
    s = si+v*t
    return s