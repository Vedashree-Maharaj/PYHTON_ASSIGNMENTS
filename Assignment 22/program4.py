# Calculate 1⁵ + 2⁵ + ... + N⁵ and Measure Execution Time using Pool

import multiprocessing
import os


def power(No):
    print("Process is Running with PId :",os.getpid())
    Sum=0
    for i in range(1,No+1):
        Sum=Sum + (i**5)
    return Sum


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    pobj=multiprocessing.Pool()

    Result=pobj.map(power,Data)

    pobj.close()
    pobj.join()


    print("Sum of all Numbers is :")
    print(Result)


if __name__=="__main__":
    main()