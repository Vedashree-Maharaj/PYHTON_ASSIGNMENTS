#program to print area of circle

def Area(Radius,PI):
    Ans=PI*Radius*Radius
    return Ans

def main():
    Radius=int(input("Enter the side:"))
    Ret=Area(Radius,3.14)
    print("Area of CIRCLE is:",Ret)

if __name__=="__main__":
    main()