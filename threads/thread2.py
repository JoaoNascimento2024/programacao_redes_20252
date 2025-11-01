import threading
import time

def imprimir():
    for i in range(10):
        print(i)
        time.sleep(1)

tt = threading.Thread(target=imprimir,)
tt.start()

ttt = threading.Thread(target=imprimir,)
ttt.start()

