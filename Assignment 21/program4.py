# Design a Python application that creates two threads.
# Thread1 should compute the sum of elements from a list.
# Thread2 should compute the product of elements from the same list.

import threading

def Addition(Data):
    Sum = 0

    for i in Data:
        Sum = Sum + i

    print("Sum of elements:", Sum)

def Multiplication(Data):
    Product = 1

    for i in Data:
        Product = Product * i

    print("Product of elements:", Product)

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    t1 = threading.Thread(target=Addition, args=(Data,))
    t2 = threading.Thread(target=Multiplication, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()