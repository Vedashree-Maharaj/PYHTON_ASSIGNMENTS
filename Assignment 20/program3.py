# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# EvenList thread should extract all even elements from the list and calculate their sum.
# OddList thread should extract all odd elements from the list and calculate their sum.
# Threads should run concurrently.

import threading

def EvenList(Data):
    Even = list(filter(lambda x: x % 2 == 0, Data))
    print("Even elements:", Even)
    print("Sum of even elements:", sum(Even))

def OddList(Data):
    Odd = list(filter(lambda x: x % 2 != 0, Data))
    print("Odd elements:", Odd)
    print("Sum of odd elements:", sum(Odd))

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()