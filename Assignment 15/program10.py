#Lambda function using filter() to return the count of even numbers

CheckEven = lambda No: No % 2 == 0

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print("Count of even numbers is:", len(FData))

if __name__ == "__main__":
    main()