# Sum of Even Numbers from 1 to N using multiprocessing.Pool

import multiprocessing
import os


def SumEven(No):
    print("Process is Running with PId :",os.getpid())
    Sum=0

    for i in range(1,No+1):
        if i % 2 ==0:
            Sum=Sum+i
    return Sum


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    pobj=multiprocessing.Pool()

    Result=pobj.map(SumEven,Data)

    pobj.close()
    pobj.join()


    print("Sum of Even Numbers is :")
    print(Result)


if __name__=="__main__":
    main()