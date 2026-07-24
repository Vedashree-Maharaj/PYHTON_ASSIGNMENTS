# program to 
"""
Accept the source file path.
Accept the destination folder path.
Create a backup every hour.
Add the current date and time to the backup file name.
Write the backup details into backup_log.txt.
Use the shutil module for copying.

""" 

import schedule
import shutil
import datetime
import time
import os

def Display(DirectoryPath = "Demo"):

    timestamp = datetime.datetime.now()

    LogFileName = "Marvellous_" + str(timestamp) + ".txt"
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    DestinationFile = os.path.join(DirectoryPath, LogFileName)

    shutil.copy("Marvellous.txt", DestinationFile)

    fobj = open("BackupLog.txt", "a")
    fobj.write("Backup completed successfully at :" + str(timestamp) + "\n")
    fobj.write("Backup File :" + DestinationFile + "\n")

    fobj.close()

def main():

    schedule.every(1).hour.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()