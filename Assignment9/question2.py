""" program contains function ChkGreater() that accepts two numbers 
and print greater  number"""

def  ChkGreater(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2
    
def main():
    No1=int(input("Enter the First number:"))
    No2=int(input("Enter the SECOND number:"))

    Ret=ChkGreater(No1,No2)
    print("The GREATER numbers is",Ret)

if __name__=="__main__":
    main()