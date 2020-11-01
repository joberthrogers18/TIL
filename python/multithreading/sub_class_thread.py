from utils import thread_delay
import threading

class ThreadingExample(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting Thread:', self.name)
        thread_delay(self.name, self.delay)
        print('Execution of Thread:', self.name, 'is complete!')

if __name__ == '__main__':
    t1 = ThreadingExample('t1', 1)
    t2 = ThreadingExample('t2', 3)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Thread execution is complete!')