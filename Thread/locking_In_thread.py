import threading
arr=[0,0]
def task(lock):
    global arr;
    for i in range(100000):
        # lock.acquire()
        arr[0]+=1
        for i in range(101):
            print(1)
        # lock.release()
    for i in range(100000):
        lock.acquire()
        arr[1] +=1
        for i in range(100000):
            if i==0:
                print(i)
            if i==99999:
                print(i)
        lock.release()


lock = threading.Lock()
t1 = threading.Thread(target=task,args =(lock,))
t2 = threading.Thread(target=task,args =(lock,))
t1.start()
t2.start()
t1.join()
t2.join()
print(arr)