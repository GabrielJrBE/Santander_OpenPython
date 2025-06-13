arquivo = None

try:
    # Codigo que pode gerar uma exceçao
    arquivo = open("arquivo.txt","r")
    # Realiza opreçoes com arquivo
except FileNotFoundError:
    print("Erro: Arquivo nao encotrado")
finally:
    if arquivo:
        arquivo.close() # Fechar o arquivo sempre, mesmo que ocorrer uma exceçao
    print("O bau foi fechado,independe do que aconteceu.")