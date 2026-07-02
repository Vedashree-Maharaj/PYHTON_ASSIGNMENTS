# program to accept one number and print cube of it

def Cube(No):
    return No*No*No

def main():
    No1=int(input("Enter the Number:"))
    Ret=Cube(No1)

    print("The Cube of Number is:",Ret)

if __name__=="__main__":
    main()