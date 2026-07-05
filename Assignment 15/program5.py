#program to use reduce for maximum of sll numbers

from functools import reduce

Maximum = lambda A, B: A if A > B else B

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    RData = reduce(Maximum, Data)

    print("Maximum number is:", RData)

if __name__ == "__main__":
    main()