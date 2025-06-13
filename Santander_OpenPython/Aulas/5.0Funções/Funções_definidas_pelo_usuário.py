# Função definida pelo usuário que calcula a média de vários números
def calcular_media(*numeros):  # *numeros permite passar vários argumentos
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Média:", calcular_media(10, 20, 30, 40))


# Função tradicional com nome e retorno
def somar_3(x):
    return x + 3

# Função lambda (anônima), usada para operações simples
somar = lambda x: x + 3

print("Somar 3 a um número:", somar(5))
