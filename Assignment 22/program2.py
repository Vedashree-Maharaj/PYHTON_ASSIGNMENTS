# Calculate Factorials of Multiple Numbers using Pool

import multiprocessing
import os


def Factorial(No):
    print("Process is Running with PId :",os.getpid())
    Fact=1

    for i in range(1,No+1):
        Fact=Fact * i
    return Fact


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    pobj=multiprocessing.Pool()

    Result=pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()


    print("Factorial of Numbers is :")
    print(Result)


if __name__=="__main__":
    main()