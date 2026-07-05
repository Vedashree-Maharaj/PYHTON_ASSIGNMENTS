# Lambda function to return minimum of two numbers

Minimum = lambda No, No1: No1 if No > No1 else No

def main():
    Value = int(input("Enter First Number: "))
    Value1 = int(input("Enter Second Number: "))

    Ret = Minimum(Value, Value1)

    print("The minimum of numbers is =", Ret)

if __name__ == "__main__":
    main()