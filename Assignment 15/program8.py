#Lambda function using filter() to return numbers divisible by both 3 and 5

Check = lambda No: No % 3 == 0 and No % 5 == 0

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    FData = list(filter(Check, Data))

    print("Numbers divisible by both 3 and 5:", FData)

if __name__ == "__main__":
    main()