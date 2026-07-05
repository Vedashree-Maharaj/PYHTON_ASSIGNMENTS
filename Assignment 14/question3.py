# Lambda function to return maximum of two numbers

Maximum = lambda No, No1: No1 if No < No1 else No

def main():
    Value = int(input("Enter First Number: "))
    Value1 = int(input("Enter Second Number: "))

    Ret = Maximum(Value, Value1)

    print("The maximum of numbers is =", Ret)

if __name__ == "__main__":
    main()