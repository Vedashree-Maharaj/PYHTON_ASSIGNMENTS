# program that scannes a specified directory every minute

import os 
import schedule
import datetime
import time

def scanDirectory(dir):
    for FolderName , Subfolder ,FileName in os.walk(dir):
        print("Directory Scanned is :",dir)
        
        print("Total Number of File : ",len(FileName))
    
        print("Total Number of SubFolder :",len(Subfolder))
        print("Scanned Time is:",datetime.datetime.now())

def main():
    directory = input("Enter directory Name: ")
    print("Automation Script Started...")
    

    schedule.every(1).minute.do(scanDirectory, directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()


        
        

