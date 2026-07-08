# Program to accept a number and check whether it is prime

def Prime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    Num = int(input("Enter the number: "))

    Ret = Prime(Num)

    if Ret == True:
        print("The number is Prime")
    else:
        print("The number is Not Prime")

if __name__ == "__main__":
    main()