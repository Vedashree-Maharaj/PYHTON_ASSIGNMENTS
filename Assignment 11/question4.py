# Program to accept a number and print its reverse

def Reverse(No):
    Rev = 0

    while No != 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    return Rev

def main():
    Num = int(input("Enter the number: "))

    Ret = Reverse(Num)

    print("Reverse number is:", Ret)

if __name__ == "__main__":
    main()