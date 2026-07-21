# program to display File contents on console


import os

def Display(Name):
    for FolderName, SubFolder, FileNames in os.walk("Directory1"):
        for File in FileNames:
            if File == Name:
                Path = os.path.join(FolderName, File)
 
                fobj = open(Path, "r")
                Data = fobj.read()
                print(Data)
                fobj.close()
                return

    print("File not found.")

def main():
    Name = input("Enter the file name: ")
    Display(Name)

if __name__ == "__main__":
    main()
