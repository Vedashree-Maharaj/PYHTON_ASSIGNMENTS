# program that creates new file every minute

import schedule
import time
import datetime

def filecreate():

    filename = "File_" + str(datetime.datetime.now()) + ".txt"
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")

    file = open(filename, "w")
    file.write("File Created Successfully\n")
    file.write("Creation Date : " + str(datetime.datetime.now().date()) + "\n")
    file.write("Creation Time : " + str(datetime.datetime.now().time()) + "\n")
    file.close()

    print(filename, "created successfully.")

def main():


    schedule.every(1).minutes.do(filecreate)

    print("Automation Script Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

