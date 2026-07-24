# program that accepts a directory name from user and counts the numbers of files inside 
#it every five minutes

import os
import time
import datetime
import schedule

def DirectoryCount(path):

    for FolderName, SubFolder, FileName in os.walk(path):

        fobj = open("DirectoryCountLog.txt", "a")

        fobj.write("Directory Path : " + FolderName + "\n")
        fobj.write("Total Files : " + str(len(FileName)) + "\n") # if not use f string insted of str()func
        fobj.write("Date and Time : " + str(datetime.datetime.now()) + "\n")
        fobj.write("---------------------------------\n")

        fobj.close()

        print("Entry Added Successfully")

def main():

    directory = input("Enter directory path : ")

    print("Automation Script Started...")

    schedule.every(5).minutes.do(DirectoryCount, directory)   

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()