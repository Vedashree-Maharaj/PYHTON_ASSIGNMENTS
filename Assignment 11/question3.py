# Program to accept a number and print the sum of digits

def Sum(No):
    Sum = 0

    while No != 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Num = int(input("Enter the number: "))

    Ret = Sum(Num)

    print("The sum of digits is:", Ret)

if __name__ == "__main__":
    main()