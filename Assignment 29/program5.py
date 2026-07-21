# program to return the frequency (count of occurance) of string

import sys

def Frequency(FileName, String):
    fobj = open(FileName, "r")

    Data = fobj.read()

    Count = Data.count(String)  # In built function

    fobj.close()

    print("Frequency of", String, "is", Count)

def main():
    FileName = sys.argv[1]
    String = sys.argv[2]

    Frequency(FileName, String)

if __name__ == "__main__":
    main()