import threading
import time

class myThread (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID= threadID
        self.name=name
        self.counter = counter
    def run(self):
        print("starting"+self.name)
        print_time(self.name, self.counter, 3)

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName,time.ctime(time.time())))
        counter -=1
        threadLock = threading.Lock()
threads = []
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)


for t in threads:
    t.join()
print("Exiting Main Thread")


#!
import threading
import time

exitFlag = 0
class mtThread(threading.Thread):
    def __init__(self,threadId,counter):
        self.threadID= threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting"+ self.name)
        print_time(self.name,2,self.counter)
        print("Exiting"+self.name)
def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print ("Exiting Main Thread")























