#program to accept one number and print square of it

def Square(No):
    return No*No

def main():
    No1=int(input("Enter the Number:"))
    Ret=Square(No1)

    print("The Square of the Number is :",Ret)
    
if  __name__ == "__main__":
    main()