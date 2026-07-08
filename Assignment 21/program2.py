# Design a Python application that creates two threads.
# Thread1 should calculate and display the maximum element from a list.
# Thread2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    print("Maximum element is:", Max)

def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    print("Minimum element is:", Min)

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()