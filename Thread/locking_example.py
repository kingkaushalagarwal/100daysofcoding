import threading
def addScore(lock):
    global score;
    lock.acquire()
    score+=1;
    lock.release()
def substractScore(lock):
    global score;
    lock.acquire()
    score-=1;
    lock.release()
class MyThread1(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        threading.Thread.__init__(self)
    def run(self):
        for i in range(100005):
            addScore(self.lock)
class MyThread2(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        threading.Thread.__init__(self)
    def run(self):
        for i in range(100000):
            substractScore(self.lock)

#Driver class
score =0
lock = threading.Lock()
t1 = MyThread1(lock)
t2= MyThread2(lock)


t1.start()
t2.start()
t1.join()
t2.join()
print(score)
