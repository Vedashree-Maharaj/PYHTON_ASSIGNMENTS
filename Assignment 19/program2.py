# program to create lambda function and retrun multiplication of two numbers

Multiplication=lambda Num1,Num2:Num1*Num2

def main():
    number1=int(input("Enter FIRST number:"))
    number2=int(input("Enter SECOND number:"))

    Ret=Multiplication(number1,number2)

    print("The Multiplication of numbers is :",Ret)

if __name__=="__main__":
    main()