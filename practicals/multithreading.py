import threading
import time

def print_num():
    for i in range(1,6):
        print(f"Numbers: {i}")
        time.sleep(1)

def print_letters():
    for i in ['A','B','C','D','E']:
        print(f"Letters: {i}")
        time.sleep(1)

t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("threads completed successfully")

