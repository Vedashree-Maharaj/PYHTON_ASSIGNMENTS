#program to print factors


def Factor(No):
    for i in range(1,No+1):
        if No % i==0:
            print( i)
        
    
def main():
    Num = int(input("Enter the number: "))

    Ret = Factor(Num)

    print("The Factors are:",Ret)

if __name__ == "__main__":
    main()
