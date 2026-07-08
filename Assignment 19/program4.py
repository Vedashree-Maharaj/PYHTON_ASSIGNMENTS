# program contains filter(),map(),reduce() in list and print even number and sqaure
#reduce() will return addition of all numbers

from functools import reduce

def CheckEven(No):
     return (No%2==0)

def Square(No):
     return No*No

def Addition(No1, No2):
     return No1 + No2

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is :", Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter :", FData)

    MData = list(map(Square, FData))
    print("Data after map :", MData)

    RData = reduce(Addition, MData)
    print("Data after reduce :", RData)

if __name__ == "__main__":
     main()