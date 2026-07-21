# program to Copy all the contents of the first file into the second file.

def CopyFile(main_file, copy):
    fmain = open(main_file, "r")
    fcopy = open(copy, "w")

    Data = fmain.read()
    fcopy.write(Data)

    fmain.close()
    fcopy.close()

def main():
    ExistingFile = input("Enter existing file name: ")
    NewFile = input("Enter new file name: ")

    CopyFile(ExistingFile, NewFile)

    print(f"Contents of { ExistingFile } copied into { NewFile} ")

if __name__ == "__main__":
    main()