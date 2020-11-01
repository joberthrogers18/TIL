import threading
import _thread
import time

def thread_delay(thread_name, delay):
    print('foi')
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '--------->', time.time())

def start_and_wait_thread_finish(*args):
    for thr in args:
        thr.start()

    for thr in args:
        # wait thread finish to execute the next lines
        thr.join()

def volume_cube(a):
    print('Volume of cube: ', a**3)

def volume_square(a):
    print('Volume of Square: ', a*a)

if __name__ == '__main__':
    _thread.start_new_thread(thread_delay, ('t1', 1))
    _thread.start_new_thread(thread_delay, ('t2', 5))
    
    t3 = threading.Thread(target=thread_delay, args=('t3', 2))
    t4 = threading.Thread(target=thread_delay, args=('t4', 3))
    
    start_and_wait_thread_finish(t3, t4)

    print('\n\nThread execution is complete!\n')

    th_volume_1 = threading.Thread(target=volume_cube, args=(2,))
    th_volume_2 = threading.Thread(target=volume_square, args=(3,))

    start_and_wait_thread_finish(th_volume_1, th_volume_2)

    print('\n\nVolumes threading are complete!\n')

    time.sleep(12000)