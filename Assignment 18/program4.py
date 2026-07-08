# program to accept N numbers in list and return frequency


def Frequency(Data, Value):
    Count = 0

    for i in Data:
        if i == Value:
            Count = Count + 1

    return Count


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    Search = int(input("Enter number to search: "))

    Ret = Frequency(Data, Search)

    print("Frequency is:", Ret)


if __name__ == "__main__":
    main()