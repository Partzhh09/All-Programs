import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,ThreadID,name,counter):
        threading.Thread.__init__(self)
        self.ThreadID =ThreadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting",+ self.name)
        print(self.name,5,self.counter)
        print("Exting",+ self.name)

    def print_time(ThreadName,counter,delay):
        while counter:
            if exitFlag:
                ThreadName.exit()
            time.sleep(delay)
            print("%s %s"%(ThreadName,time.ctime(time.time())))
            counter -= 1

            thread1 = myThread(1,"Thread-1",1)
            thread2 = myThread(2,"thread-2",2)

            thread1.start()
            thread2.start()

            print("Exiting main thread")