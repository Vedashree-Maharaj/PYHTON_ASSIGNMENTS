# Program to check whether a number is divisible by 5

def ChkNum(Num):
    if Num % 5 == 0:
        return True
    else:
        return False

def main():
    Number = int(input("Enter the number: "))

    Ret = ChkNum(Number)

    if Ret == True:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()


"""OR

def ChkNum(Num):
    return Num % 5 == 0

def main():
    Number = int(input("Enter the number: "))

    print(ChkNum(Number))

if __name__ == "__main__":
    main()
"""