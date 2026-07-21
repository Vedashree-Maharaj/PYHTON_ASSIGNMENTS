# program which accepts a file name from the user and display line by line 

def CountLines(FileName):
    try:
        file = open(FileName, "r")

        for line in file:
            
                print(line)
    
    except Exception as eobj :
        print("Exception occured",eobj)

    

def main():
    Name = input("Enter file name: ")

    CountLines(Name)

if __name__ == "__main__":
    main()