# program to create new log file after every 10 mins

import time
import datetime
import schedule

def Display():

    timestamp = datetime.datetime.now()

    LogFileName = "Marvellous_" + str(timestamp) + ".txt"
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    fobj = open(LogFileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time: " + str(timestamp))

    fobj.close()

    print(LogFileName, "created successfully.")

def main():

    print("Automation Script Started...")
    
    schedule.every(10).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    