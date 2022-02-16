import threading
import time

class myThread(threading.thread):
    def_init_(self,thread,name,counter):
        threading.thread._init_(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print"starting" + self.name
        #get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter,3)
        #free lock to release next thread
        threadLock.release()

    def print_time(threadName, delay, counter):
        white counter:
            time.sleep(delay)
            print("%s: %s" %(threadName,time.ctime(time.time()))
                  counter -= 1
                  #counter = counter - 1

    threadLock = thread.Lock()
    threads = []

    # create new threads
    thread1 = myThread(1, "thread-1", 1)
    thread2 = myThread(2, "thread-2", 2)

    # Start new threads
    thread1.start()
    thread2.start()

    # add thread to thread list
    threads.append(thread1)
    threads.append(thread2)


    # wait for all threads to complete

    for t in thraedsL:
                  t,join()
                  print"Exiting main thread"

                  
