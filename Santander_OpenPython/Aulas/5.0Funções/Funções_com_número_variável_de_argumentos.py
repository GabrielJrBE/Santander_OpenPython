def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1,2,3))
print(soma_variavel(4,5,6,7))
