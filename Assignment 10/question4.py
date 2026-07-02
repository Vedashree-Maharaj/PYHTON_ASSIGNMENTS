#program to accept the number and print the even number till that number

def Even(No):
    for i in range(0,No+1):
        if i%2==0:
            
            print(i)
        
def main():
    Num=int(input("Enetr the number:"))

    print("The even number are:")
    Even(Num)

if __name__=="__main__":
    main()