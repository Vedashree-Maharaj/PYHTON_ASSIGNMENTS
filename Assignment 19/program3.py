# program contains filter(),map(),reduce() in list and print number greater or equal to 70and less than equal to 90
#reduce() will return product of all numbers

from functools import reduce

def CheckEven(No):
     return (No >= 70 and No <= 90)

def Increment(No):
     return No + 10

def Multiplication(No1, No2):
     return No1 * No2

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is :", Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter :", FData)

    MData = list(map(Increment, FData))
    print("Data after map :", MData)

    RData = reduce(Multiplication, MData)
    print("Data after reduce :", RData)

if __name__ == "__main__":
     main()