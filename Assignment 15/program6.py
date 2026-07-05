#program to use reduce for minimum of sll numbers

from functools import reduce

Minimum = lambda A, B: B if A > B else A

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    RData = reduce(Minimum, Data)

    print("Minimum number is:", RData)

if __name__ == "__main__":
    main()