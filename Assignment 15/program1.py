#program of lambda function using map to accept list and return its square of each number

Square = lambda No: No * No

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    MData = list(map(Square, Data))

    print("Squares are:", MData)

if __name__ == "__main__":
    main()