#program to accept number and print that many numbers before that number

def Number(No):
    for i in range(0,No):
        print(i)

def main():
    no1=int(input("Enter the number:"))

    print("Numbers are:")
    Number(no1)

if __name__=="__main__":
    main()


