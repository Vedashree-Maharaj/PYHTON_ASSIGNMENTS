#program of accepting one number and print multiplication table
 
def Table(No):
    for i in range(1, 11):
        print( No * i)

def main():
    No1 = int(input("Enter the Number: "))
    
    print("The Multiplication Table is:")
    Table(No1)

if __name__ == "__main__":
    main()