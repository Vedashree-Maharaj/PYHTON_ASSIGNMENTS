# program t check if file present in directory


import os

def Existance(File):
    for FolderName, SubFolder, FileName in os.walk("Directory1"):
        for Name in FileName:
            if Name == File:
                return True

    return False

def main():
    Name = input("Enter the file to search in Directory: ")

    Ret = Existance(Name)

    if Ret == True:
        print("The file is present in the directory.")
    else:
        print("The file is not present in the directory.")

if __name__ == "__main__":
    main()