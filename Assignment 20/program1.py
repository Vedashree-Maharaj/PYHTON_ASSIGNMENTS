#program for twothreads one for first 10 even number and another for odd

import threading

def SumEven():
    print("Even numbers are:")
    for i in range(2, 21, 2):
        print(i)

def SumOdd():
    print("Odd numbers are:")
    for i in range(1, 20, 2):
        print(i)

def main():
    t1 = threading.Thread(target=SumEven)
    t2 = threading.Thread(target=SumOdd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()