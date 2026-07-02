#program to print area of rectangle

def Area(length,breadth):
    Ans=length*breadth
    return Ans

def main():
    side1=int(input("Enetr length:"))
    side2=int(input("Enetr breadth:"))

    Ret=Area(side1,side2)
    print("Area of Rectangle is:",Ret)

if __name__=="__main__":
    main()