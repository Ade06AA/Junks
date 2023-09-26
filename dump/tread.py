#!/usr/bin/python3
import threading
import time
i = 0

def p():
    global i
    while True:
        time.sleep(1)
        print(i)
threading.Thread(target=p).start()

while True:
    i += 1
    time.sleep(0.5)

