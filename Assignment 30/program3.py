# program to print " Coding Kar..!" after every 30 mins

import schedule
import time

def Coding():
    print("Coding Kar... !")

def main():
    print("Automation Script Started...")
    schedule.every(30).minutes.do(Coding)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ =="__main__":
    main()
