# program which accepts a file name from the user and counts how many words are in file

def CountLines(FileName):
    try:
        file = open(FileName, "r")

        Count = 0

        for line in file:
            for word in line:
                Count = Count + 1

    
        return Count
    
    except Exception:
        print("Exception occured")

    

def main():
    Name = input("Enter file name: ")

    Ret = CountLines(Name)

    print("Number of words in the file:", Ret)


if __name__ == "__main__":
    main()