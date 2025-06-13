"""As listas de compreensão são uma forma concisa de criar novas listas
baseadas em uma sequência existente. Permitem filtrar e transformar
os elementos de uma lista em uma única linha de código."""
#nova_lista = [expressão for elemento in sequência if condição]

numeros = [1,2,3,4,5]
quadrado = [x**2 for x in numeros if x % 2 == 0]
print(quadrado)