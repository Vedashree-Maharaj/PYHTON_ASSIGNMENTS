#program to accept number and print factorial

def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i

    return Fact

def main():
    Num=int(input("Enter the number:"))

    Ret=Factorial(Num)

    print("The Factorial is :",Ret)

if __name__=="__main__":
    main()
