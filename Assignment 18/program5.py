# program to accept N numbers in list and return prime num with importing module

import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for i in Data:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    Ret = ListPrime(Data)

    print("Addition of prime numbers is:", Ret)


if __name__ == "__main__":
    main()