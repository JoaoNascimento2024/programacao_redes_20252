import datetime

lista_enderecos_ip = []

while True:
    endereco_ip = input("Digite um endereço IP: ")
    if endereco_ip.lower() == "fim":
        break
    lista_enderecos_ip.append(endereco_ip)

agora = datetime.datetime.now()
data_hora_formatada = agora.strftime("%Y%m%d %H%M%S")

arquivo = open(f"C:\\temp\\{data_hora_formatada}.txt","w")
for endereco_ip in lista_enderecos_ip:
    print(endereco_ip)    
    arquivo.write(f"{endereco_ip}\n")

arquivo.close()