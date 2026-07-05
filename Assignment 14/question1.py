# lambda function return square

Square= lambda No: (No * No) 

def main():
    Value=int(input("Enter NUmber:"))
    Ret=Square(Value) 

    print("The Square of number is =",Ret)

if __name__ == "__main__":
    main()