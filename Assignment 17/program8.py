"""program to accept number and print pattern
 Ex ---> Input --> 5
         Output --> 1 
                    1 2 
                    1 2 3
                    1 2 3 4 
                    1 2 3 4 5
"""

def Pattern1(Num):
    for i in range(1,Num+1):
        for j in range(1,i+1):
            print(j,end=" ")  
        print()   
 
def main():
    Num1=int(input("Enter the number:"))

    Pattern1(Num1)


if __name__ =="__main__":
    main()