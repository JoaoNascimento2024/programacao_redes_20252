import os

path = r"D:\programacao_redes_20252\lista1>"

arquivos = os.listdir(path)

for arquivo in arquivos:
  if arquivo[-3:] == ".py":
    print(arquivo)