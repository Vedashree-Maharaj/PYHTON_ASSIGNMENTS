# program contains Add() accept two numberss and return addition 

def Add(Num1,NUm2):
    return Num1 + NUm2

def main():
    N1=int(input("Enter the 1st number:"))

    N2=int(input("Enter the 2nd number:"))

    Ret=Add(N1,N2)

    print("Addition is :",Ret)

if __name__=="__main__":
    main()

