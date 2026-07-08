# program contains filter(),map(),reduce() in list and print prime number and multiply each num by 2
#reduce() will return product of all numbers

from functools import reduce

def CheckPrime(No):
     if No <= 1:
        return False

     for i in range(2, No):
         if No % i == 0:
             return False

     return True

def Increment(No):
     return No*2

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

    return Max
def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is :", Data)

    FData = list(filter(CheckPrime, Data))
    print("Data after filter :", FData)

    MData = list(map(Increment, FData))
    print("Data after map :", MData)

    RData = reduce(Maximum, MData)
    print("Data after reduce :", RData)

if __name__ == "__main__":
     main()