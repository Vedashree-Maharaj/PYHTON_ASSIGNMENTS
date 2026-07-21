# program which accepts a file name from the user and counts how many lines are in file

def CountLines(FileName):
    try:
        file = open(FileName, "r")

        Count = 0

        for line in file:
            Count = Count + 1

        file.close()

        return Count
    
    except Exception as eobj:
        print("Exception occured",eobj)

    

def main():
    Name = input("Enter file name: ")

    Ret = CountLines(Name)

    print("Number of lines in the file:", Ret)


if __name__ == "__main__":
    main()