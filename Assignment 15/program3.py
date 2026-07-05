# Program of lambda function using filter to accept a list and return odd numbers

CheckOdd = lambda No: No % 2 != 0

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    FData = list(filter(CheckOdd, Data))

    print("Odd numbers are:", FData)

if __name__ == "__main__":
    main()