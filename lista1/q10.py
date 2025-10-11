import os

path = "c:\\y\\"

nome_pasta = input("Digite o nome da pasta: ")

#os.mkdir(f"{path}{nome_pasta}")
os.makedirs(path + nome_pasta)