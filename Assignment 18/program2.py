# program to accept N numbers in list and return maximum

def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    return Max


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    Ret = Maximum(Data)

    print("Maximum number is:", Ret)


if __name__ == "__main__":
    main()