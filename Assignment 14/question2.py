# lambda function return cube

Cube= lambda No: (No * No * No) 

def main():
    Value=int(input("Enter NUmber:"))
    Ret=Cube(Value) 

    print("The Cube of number is =",Ret)

if __name__ == "__main__":
    main()