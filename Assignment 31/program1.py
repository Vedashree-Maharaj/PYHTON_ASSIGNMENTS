# program that accepts
# 1) A message from user
# 2) A time interval in seconds
# schdedule the program to display message repeatedly after the specified interval

import schedule
import time

def Display(Message):
    print(Message)

def main():

    Message = input("Enter the message: ")

    Interval = int(input("Enter interval in seconds: "))

    if Interval <=0:
        print("Interval must be greater than zero")

    else:
        print("Automation Script Started...")

        schedule.every(Interval).seconds.do(Display, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()