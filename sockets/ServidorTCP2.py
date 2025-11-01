import socket
import threading

def tratar_conn(conn, address):
    while True:
        mensagem = conn.recv(1024)
        print(f"Mensagem: {mensagem.decode()} - Endereco: {address}")
        conn.sendall("Recebido com sucesso".encode())    

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 5000))
servidor.listen()
print("Servidor conectado!!!")

while True:
    conn, address = servidor.accept()
    thread = threading.Thread(target=tratar_conn, args=(conn, address),)
    thread.start()


