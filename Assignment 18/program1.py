# program to accept N numbers in list and return addition

def AddList(Num):
    Sum=0
    for i in Num:
        Sum=Sum+i
    return Sum

def main():
    Number=[]
    Size = int(input("Enter number of elements: "))
    
    for i in range(Size):
        No = int(input("Enter number: "))
        Number.append(No)
    
    Ret=AddList(Number)

    print("Sum of all digits in list is:",Ret)

if __name__=="__main__":
    main() 