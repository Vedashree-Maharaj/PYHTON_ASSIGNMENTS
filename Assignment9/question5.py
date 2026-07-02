# program to accept number and check if divisible by 3 and 5

def Divisor(no):
    if (no%3==0 and no%5==0):
        return True
    else:
        return False
    
def main():
    No1=int(input("Eneter the number:"))
    Ret=Divisor(No1)
    
    if Ret==True:
        print("The number is Divisible by 3 and 5")
    else:
        print("The number is not Divisible by 3 and 5")

if __name__=="__main__":
    main()