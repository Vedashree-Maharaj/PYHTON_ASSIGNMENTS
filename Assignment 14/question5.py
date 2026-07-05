# lambda function return true if num is even else false

Even = lambda No: True if No % 2==0 else False

def main():
    Value = int(input("Enter the Number: "))
    
    Ret = Even(Value)

    print( Ret)

if __name__ == "__main__":
    main()