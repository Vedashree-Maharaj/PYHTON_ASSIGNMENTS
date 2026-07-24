# program that moniters size of file every 30 mins

import os
import schedule
import time
import datetime

def filecreate(path):

    try:
        
        fobj = open("FileSizeLog.txt", "a")

        fobj.write("File Path : " + path + "\n")
        fobj.write("File Size : " + str(os.path.getsize(path)) + " Bytes\n")
        fobj.write("Date : " + str(datetime.datetime.now().date()) + "\n")
        fobj.write("Time : " + str(datetime.datetime.now().time()) + "\n")
        fobj.write("-----------------------------------\n")

        fobj.close()

        print("Information added successfully.")

    except FileNotFoundError:
        print("File does not exist.")

def main():

    path = input("Enter file path : ")

    schedule.every(3).seconds.do(filecreate, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()