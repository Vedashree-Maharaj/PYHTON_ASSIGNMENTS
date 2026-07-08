#program to accept number and print pattern
""""
 Ex ---> Input --> 5
         Output --> * * * * *
                    * * * * 
                    * * *
                    * * 
                    *
"""

def Pattern1(Num):
    for i in range(Num):
        for j in range(i,Num):
            print("*",end=" ")  
        print()   
 
def main():
    Num1=int(input("Enter the number:"))

    Pattern1(Num1)


if __name__ =="__main__":
    main()