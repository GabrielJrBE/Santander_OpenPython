# Operações com conjuntos: união (|), interseção (&), diferença (-) e diferença simétrica (^)

frutas = {"maça","banana","laranja"}
numeros = set ([1,2,3,4,5])

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

uniao = conjunto1 | conjunto2
print(uniao) #imprime {1,2,3,4,5}

intersecao = conjunto1 & conjunto2
print(intersecao) #imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca) # imprime {1,2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)


