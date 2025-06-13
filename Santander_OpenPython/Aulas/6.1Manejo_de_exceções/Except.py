
try:
    # Codigo que pode gerar um excecao
    resultado = 10/0 # Divisao por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisao por zero")
except ValueError:
    print("Erro: Valor invalido")