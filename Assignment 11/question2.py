# Program to accept a number and count the digits using for loop

def Count(No):
    Count = 0

    while No != 0:
        Count = Count + 1
        No = No // 10

    return Count

def main():
    Num = int(input("Enter the number: "))

    Ret = Count(Num)

    print("The count of digits is:", Ret)

if __name__ == "__main__":
    main()