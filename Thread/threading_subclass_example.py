import threading
def display():
    for i in range(1,100):
        print(i,end=" ")
    print()
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        display()
#Driver
t1 = MyThread()
t2 = MyThread()
t1.start()
t2.start()
t1.join()
t2.join()