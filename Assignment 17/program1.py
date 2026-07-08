# program to access module with arithmetic operations

import ModuleOperation

def main():
    print("Enter FIRST number:")
    Value1=int(input())

    print("Enter SECOND number:")
    Value2=int(input())

    Ret=ModuleOperation.Add(Value1,Value2)
    Ret1=ModuleOperation.Sub(Value1,Value2) 
    Ret2=ModuleOperation.Mul(Value1,Value2) 
    Ret3=ModuleOperation.Div(Value1,Value2) 

    print("Addition is:",Ret)
    print("Substraction is:",Ret1)
    print("Multiplication is:",Ret2)
    print("Division is:",Ret3)

if __name__=="__main__":
    main()

