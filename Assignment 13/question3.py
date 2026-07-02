#program to check number is perfect or not
#perfect number is the number which is equalv to sum of its factors excluding the number

def PerfectNumber(No):
    Count=0
    for i in range(1,No):
        if No % i==0:
           Count=Count+i
    return Count 

def main():
    Num=int(input("Enter the number:"))

    Ret=PerfectNumber(Num)

    if Ret == Num:
        print("The given number is a Perfect Number")
    else:
        print("The given number is NOT a Perfect Number")
        
if __name__ == "__main__":
    main()