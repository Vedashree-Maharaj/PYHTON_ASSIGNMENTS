# progarm to create function ChkNum() and check num is odd or even

def ChkNum(Num):
    if Num % 2==0:
        return True
    else:
        return False
    
def main():
    Number=int(input("Enter the number:"))

    Ret=ChkNum(Number)
    if Ret==True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ =="__main__":
    main()

