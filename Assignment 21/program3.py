# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading

Counter = 0
lock = threading.Lock()

def Increment():
    global Counter

    for i in range(100000):
        lock.acquire()
        Counter += 1
        lock.release()

def main():

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter Value:", Counter)

if __name__ == "__main__":
    main()