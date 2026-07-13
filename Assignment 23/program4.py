# Count Odd Numbers between 1 and N using Pool.map()


import multiprocessing
import os


def CountOdd(No):
    print("Process is Running with PId :",os.getpid())
    Count=0

    for i in range(1,No+1):
        if i % 2 !=0:
           Count=Count + 1
    return Count


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    pobj=multiprocessing.Pool()

    Result=pobj.map(CountOdd,Data)

    pobj.close()
    pobj.join()


    print("Count of Odd Numbers is :")
    print(Result)


if __name__=="__main__":
    main()