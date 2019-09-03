import threading
from os.path import Object


class Reader_writer(Object):
    "Reader - writer solution using two monitors"

    def __init__(self):
        self.readers = 0
        self.busy = False  # writer test
        self.OKtoRead = threading.Condition()
        self.OKtoWrite = threading.Condition()
        self.mutex = threading.Lock()

    def reader(self, lastread):
        "Reader of readers and writers algorithm"
        self.OKtoRead.acquire()
        self.mutex.acquire()
        while self.busy:
            self.mutex.release()
            self.OKtoRead.wait()
            self.mutex.acquire()
        self.readers += 1
        self.mutex.release()
        self.OKtoRead.notify()
        self.OKtoRead.release()
        # Once one reader can start, they all can start.
        # --------------------------
        # critical section

        self.OKtoRead.acquire()
        self.mutex.acquire()
        self.readers = self.readers - 1
        if self.readers == 0:
            self.OKtoWrite.acquire()
            self.OKtoWrite.notify()
            self.OKtoWrite.release()
        self.mutex.release()
        self.OKtoRead.release()
        return Reader_writer

    def writer(self, data):
        "Writer of readers and writers algorithm"
        self.OKtoWrite.acquire()
        self.mutex.acquire()
        while self.busy or self.readers > 0:
            self.mutex.release()
            self.OKtoWrite.wait()
            self.mutex.acquire()
        self.busy = True
        self.mutex.release()
        self.OKtoWrite.release()
        # --------------------------
        #
        # critical section
        #
        # --------------------------
        self.OKtoWrite.acquire()
        self.OKtoRead.acquire()
        self.mutex.acquire()
        self.busy = False
        self.mutex.release()
        self.OKtoWrite.notify()
        self.OKtoWrite.release()
        self.OKtoRead.notify()
        self.OKtoRead.release()
