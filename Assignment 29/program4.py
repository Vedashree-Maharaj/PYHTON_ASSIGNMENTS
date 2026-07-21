# Program to compare two files using command line arguments

import sys

def CompareFile(File1, File2):
    fobj1 = open(File1, "r")
    fobj2 = open(File2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if Data1 == Data2:
        return True
    else:
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py File1 File2")
        return

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    Ret = CompareFile(File1, File2)

    if Ret == True:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()