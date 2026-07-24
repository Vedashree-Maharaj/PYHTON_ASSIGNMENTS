# program to schedule messages

import time 
import schedule

def monday():
    print("9.00 AM :- Start your Weekly Goals")

def wednesday():
    print("5.00 PM :- Review your weekly Progress")

def friday():
    print("6.00 PM :- Weekly work Completed")

def main():
    print("Automation Script Started...")
    
    schedule.every().monday.at("9:00").do(monday)
    schedule.every().wednesday.at("17:00").do(wednesday)
    schedule.every().friday.at("18:00").do(friday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()