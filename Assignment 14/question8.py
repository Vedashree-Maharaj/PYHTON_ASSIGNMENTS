# lambda function return addition of two numbers

Add=lambda No1,No2:No1+No2

def main():
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    
    Ret=Add(Num1,Num2)  

    print("Addition is:",Ret)

if __name__ =="__main__":
    main()