import threading
import time

def imprimir_nome_thread(nome, tempo):
    while True:        
        time.sleep(tempo) #2 segundos
        print(nome)

for i in range(5):
    thread = threading.Thread(target=imprimir_nome_thread, 
                              args=(f"Thread {i+1}", i + 1, ))
    thread.start()