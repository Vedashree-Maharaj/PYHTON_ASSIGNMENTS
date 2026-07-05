#Lambda function using reduce() to return the product of all elements

from functools import reduce

Product = lambda A, B: A * B

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    RData = reduce(Product, Data)

    print("Product of all numbers is:", RData)

if __name__ == "__main__":
    main()