#Lambda function using filter() to return strings having length greater than 5

CheckLength = lambda Str: len(Str) > 5

def main():
    Data = []

    Size = int(input("Enter number of strings: "))

    for i in range(Size):
        Str = input("Enter string: ")
        Data.append(Str)

    print("Input Data is:", Data)

    FData = list(filter(CheckLength, Data))

    print("Strings having length greater than 5:", FData)

if __name__ == "__main__":
    main()