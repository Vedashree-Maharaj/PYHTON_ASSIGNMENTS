# program to create task that executes everyday at 9:00 AM and prints: "Namaskar..."

import schedule
import time

def Message():
    print("Namaskar...")

def main():
    print("Automation Script Started...")
    schedule.every().day.at("9:00").do(Message)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ =="__main__":
    main()

