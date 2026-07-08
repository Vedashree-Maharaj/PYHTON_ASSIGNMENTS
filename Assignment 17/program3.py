# program to return factorial

def Factorial(Num):
    Fact=1
    for i in range(1,Num+1):
        Fact=Fact*i
    return Fact
    
def main():
    number=int(input("Enter the number:"))

    Ret=Factorial(number)

    print("The Factorial is:",Ret)

if __name__ =="__main__":
    main()