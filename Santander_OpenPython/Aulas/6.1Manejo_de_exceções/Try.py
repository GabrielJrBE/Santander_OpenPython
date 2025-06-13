
try:
    # Codigo que pode gerar uma excecao
    resultado = 10/0 # Divisao por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisao por zero")