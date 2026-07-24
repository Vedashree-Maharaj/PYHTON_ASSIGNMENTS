# program that displays the current date and time after every one minute

import schedule
import time
import datetime

def current_time():

    # To print in proper syntax use 
    """
    current=atetime.datetime.now()
    print("Current Date and Time:", current.strftime("%d-%m-%Y %I:%M:%S %p"))  
      strftime("%d-%m-%Y %I:%M:%S %p") → Formats the date and time as:
        WHERE:-
                %d → Day
                %m → Month
                %Y → Year
                %I → Hour (12-hour format)
                %M → Minutes
                %S → Seconds
                %p → AM/PM
    
    """
    print(f"Current Date and Time : {datetime.datetime.now()} ")

def main():
    print("Automation Script Started...")
    schedule.every(1).minute.do(current_time)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()