# Count Prime Numbers between 1 and N using multiprocessing.Pool

import multiprocessing
import os

def Prime(No):
    print("Process is Running with PId :",os.getpid())

    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def PrimeCount(N):
    Count = 0

    for i in range(2, N + 1):
        if Prime(i):
            Count += 1
    return Count   

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    pobj=multiprocessing.Pool()

    Result=pobj.map(PrimeCount,Data)

    pobj.close()
    pobj.join()


    print("Count of Prime Numbers is :")
    print(Result)


if __name__=="__main__":
    main() 