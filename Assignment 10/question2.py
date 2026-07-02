#program to accept numbrer and print the sum of all N natural numbers 

def Sum(No):
    total=0
    for i in range(1,No+1):
        total=total+i
    return total

def main():
    No=int(input("Enter the number:"))

    Ret=Sum(No)

    print("The sum of N numbers is:",Ret)

if __name__ =="__main__":
    main()


