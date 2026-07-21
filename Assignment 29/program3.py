 # Program to copy file contents into another file using command line arguments

import sys

def CopyFile(MainFile, CopyFile):
    fmain = open(MainFile, "r")
    fcopy = open(CopyFile, "w")

    Data = fmain.read()
    fcopy.write(Data)

    fmain.close()
    fcopy.close()

def main():
    
    ExistingFile = sys.argv[1]
    NewFile = sys.argv[2]

    CopyFile(ExistingFile, NewFile)

    print("Contents copied successfully.")

if __name__ == "__main__":
    main()