import time
import threading
counter = 0

def func1():
    global counter 
    while True:
        counter += 1
        counter -= 1
        time.sleep(0.8)
        print(counter)


def func2():
    global counter 
    while True:
        counter += 1
        counter -= 1
        time.sleep(0.01)
        print(counter)

threading.Thread(target=func1).start()
threading.Thread(target=func2).start()

