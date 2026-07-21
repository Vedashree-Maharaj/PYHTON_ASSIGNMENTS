# program to Search a Word in File.

def SearchWord(FileName, Word):
    fobj = open(FileName, "r")

    Data = fobj.read()

    if Word in Data:
        print(Word, "is present in the file.")
    else:
        print(Word, "is not present in the file.")

    fobj.close()

def main():
    FileName = input("Enter file name: ")
    Word = input("Enter the word to search: ")

    SearchWord(FileName, Word)

if __name__ == "__main__":
    main()