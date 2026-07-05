# lambda function return true if num is divisible by 5

Divisior = lambda No: True if No % 5==0 else False

def main():
    Value = int(input("Enter the Number: "))
    
    Ret = Divisior(Value)

    print( Ret)

if __name__ == "__main__":
    main()