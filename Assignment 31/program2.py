# program that accepts message from user and schedule

import schedule
import time

def DisplayMessage(Message):
    print(Message)

def main():

    Message = input("Enter the message: ")

    Interval = int(input("Enter interval in seconds: "))

    if Interval <=0:
        print("Interval must be greater than zero")

    else:
        print("Automation Script Started...")

        schedule.every(5).seconds.do(DisplayMessage, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()