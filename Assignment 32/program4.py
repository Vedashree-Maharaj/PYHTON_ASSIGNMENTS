# program to copy all .txt filr from onr directory to another after every ten mi utes

import os
import time
import schedule

def ReadFile(Source,Destination):
    try:
        
        fobj = open(Source, "r")

        fobj1=open(Destination,"w")
        source1 = Source.read()
        Destination.write(source1)

        fobj.close()
        fobj1.close()


    except FileNotFoundError:
        print("Error: File does not exist.")

    


def main():
    source = input("Enter source file  name: ")
    destination=input("Enter the destination file name :")

    print("Copying the file...")

    schedule.every(10).minutes.do(ReadFile, source,destination)

   
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()