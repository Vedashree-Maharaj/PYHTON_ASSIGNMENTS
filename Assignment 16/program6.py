# program to check number is positive or negative or zero

def ChkPositive(Num):
    if Num > 0:
        print("The number is Positive")
    elif Num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")
    
def main():
    Number=int(input("Enter the number:"))

    ChkPositive(Number)


if __name__ =="__main__":
    main()
