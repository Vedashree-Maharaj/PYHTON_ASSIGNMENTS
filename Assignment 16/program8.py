# program to accept number and print "*"

def Star(Num):
    for i in range(Num):
        print("*",end=" ")
    
def main():
    Number=int(input("Enter the number:"))

    Star(Number)


if __name__ =="__main__":
    main()