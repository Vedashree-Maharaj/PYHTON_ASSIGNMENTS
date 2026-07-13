# Sum of Squares from 1 to N using Pool.map()

import multiprocessing
import os


def SumCube(No):
    print("Process is Running with PId :",os.getpid())
    Sum=0

    for i in range(1,No+1):
        Sum=Sum+(i**2)
    return Sum


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    pobj=multiprocessing.Pool()

    Result=pobj.map(SumCube,Data)

    pobj.close()
    pobj.join()


    print("Sum of Cube of Numbers is :")
    print(Result)


if __name__=="__main__":
    main()