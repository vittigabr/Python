def aumentar(n, p):
    """-> Usado para adicionar alguma porcentagem de valor
    n = é o valor que será utilizado como base
    p = porcentagem que será adicionado
    """
    porcento = p/100
    aumento = n*porcento
    return moeda(aumento+n)

def dobro(n):
    """-> Usado dobrar um valor
    n = é o valor que será dobrado
    """
    dobrar = n*2
    return moeda(dobrar)

def metade(n):
    """-> Usado para descobrir a metade de qualquer valor
    n = é o valor que será dividido pela metade
    """
    dividir = n/2
    return moeda(dividir)

def diminuir(n, p):
    """-> Usado para dar desconto de qualquer valor
    n = é o valor que será utilizado como base
    p = porcentagem que será descontado
    """
    porcento = p/100
    diminui = n*porcento
    return moeda(n-diminui)

def moeda(n):
    """-> Usado para transformar qualquer valor em forma de monetário
    n = é o valor que será transformado
    """
    monetario = float(n)
    return f'{monetario:.2f}'

def resumo(cod):
    """-> Usado para mostrar o que cada função do moeda.py faz
    [] resumo(aumentar)
    [] resumo(diminuir)
    [] resumo(metade)
    [] resumo(moeda)
    [] resumo(dobro)
    """
    return help(cod)
