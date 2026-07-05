#program to use reduce for addition of sll numbers

from functools import reduce

Addition = lambda A, B: A + B

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    Result = reduce(Addition, Data)

    print("Addition of all numbers is:", Result)

if __name__ == "__main__":
    main()