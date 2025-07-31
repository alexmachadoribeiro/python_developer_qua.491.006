# função
def fatorial(n):
    # n!
    return 1 if n == 0 else n * fatorial(n-1)