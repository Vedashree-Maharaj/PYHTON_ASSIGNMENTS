# Program to check whether a number is palindrome

def Palindrome(No):
    Temp = No
    Rev = 0

    while No != 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    if Temp == Rev:
        return True
    else:
        return False

def main():
    Num = int(input("Enter the number: "))

    Ret = Palindrome(Num)

    if Ret == True:
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")

if __name__ == "__main__":
    main()