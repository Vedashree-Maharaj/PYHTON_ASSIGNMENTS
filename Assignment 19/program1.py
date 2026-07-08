# program to create lambda function which returns power of two

Power=lambda Num:Num ** 2

def main():
    number=int(input("Enter the number:"))

    Ret=Power(number)

    print("The number after calculating power of two is :",Ret)

if __name__=="__main__":
    main()