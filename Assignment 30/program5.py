# program to schedule task evevry five minutes r=that should write current date and time into file named:
#"Marvellous.txt"
# New entries should be appended without removing previous entries

import schedule 
import datetime
import time

def File_Content():
    fobj=open("Marvellous.txt","a")
    fobj.write(f"Task Executed at: {datetime.datetime.now()}\n")
    fobj.close()

def main():
    print("Automation Script Started...")
    schedule.every(5).minutes.do(File_Content)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()