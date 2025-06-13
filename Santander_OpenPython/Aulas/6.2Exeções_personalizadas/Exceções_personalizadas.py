def funcao():
    # Codigo que pode gerar uma exceçao personalizada
    if condicao:
        raise Exception("Desciçao de erro")

try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")