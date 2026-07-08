# program to accept number and return addition of factors

def FactorAdd(Num):
    Sum=0
    for i in range(1,Num): #12
        if Num % i==0: # i = 1 2 3 4 6 
            Sum=Sum + i #sum=16
    return Sum
    
def main():
    number=int(input("Enter the number:"))

    Ret=FactorAdd(number)

    print("The Addition of Factors is:",Ret)

if __name__ =="__main__":
    main()
        
