# program to schedule following tasks both should be handled by different functions
"""
1) print Lunch Time ! everydat at 1:00 PM
2) print Wrap Up Work everyday at 6:00 PM

"""

import schedule
import time
import datetime

def Lunch_time():
    print("Lunch Time ! ")

def Wrap_up():
    print("Wrap up Work...")

def main():
    print("Automation Script Started...")
    schedule.every().day.at("13:00").do(Lunch_time)
    schedule.every().day.at("18:00").do(Wrap_up)

    while True:
        schedule.run_pending()
        time.sleep(3)

if __name__ == "__main__":
    main()