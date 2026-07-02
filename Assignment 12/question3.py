#program to accept the two numbers aand perform addition subtraction multiplication and division

def Addition(No1,No2):
      Ans=0
      Ans=No1+No2
      return Ans

def Subtraction(No1,No2):
      Ans=0
      Ans=No1-No2
      return Ans

def Mul(No1,No2):
      Ans=0
      Ans=No1*No2
      return Ans

def Division(No1,No2):
      Ans=0
      Ans=No1/No2
      return Ans


def main():
    print("Enter FIRST number:")
    Value1=int(input())

    print("Enter SECOND number:")
    Value2=int(input())

    Ret1=Addition(Value1,Value2)
    Ret2=Subtraction(Value1,Value2)
    Ret3=Mul(Value1,Value2)
    Ret4=Division(Value1,Value2)

    print("Addition is:",Ret1)
    print("Subtraction is:",Ret2)
    print("Multiplication is:",Ret3)
    print("Division is:",Ret4)


if __name__=="__main__":
        main()

