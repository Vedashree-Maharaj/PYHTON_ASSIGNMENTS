# lambda function print multiplication of two numbers

Mul=lambda No1,No2: No1*No2

def main():
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    
    Ret=Mul(Num1,Num2)  

    print("Multiplication is:",Ret)

if __name__ =="__main__":
    main()