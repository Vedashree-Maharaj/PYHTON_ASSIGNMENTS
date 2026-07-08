# program to accept N numbers in list and return minimum


def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    return Min


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    Ret = Minimum(Data)

    print("Minimum number is:", Ret)


if __name__ == "__main__":
    main()