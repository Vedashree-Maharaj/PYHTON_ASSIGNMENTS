# program to delete duplicate file  automation using python

import sys
import os
import hashlib  # contains all functions to calculate Checksum
import time
import schedule
import smtplib
from email.message import EmailMessage

def CalculateChecksum(FileName):
    
    fobj=open(FileName,"rb") # rb --> "r" is read mode and "b" is binary mode

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Duplicate={}
    Ret=False
    Ret=os.path.exists(DirectoryName)

    if Ret == False:
        print("'Path is Invalid")
        return

    Ret=os.path.isdir(DirectoryName)
    
    if Ret==False:
        print("It is not a Directory")

    Unique=0
    Same=0

    for FolderNmae, SubFolder , FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderNmae,fname)
            Checksum=CalculateChecksum(fname)

            if(Checksum in Duplicate):
                Same=Same+1
                Duplicate[Checksum].append(fname)

            else:
                Unique=Unique+1
                Duplicate[Checksum]=[fname]

    return Duplicate
    
def DeleteDuplicate(DirectoryName):

    timestamp = time.ctime()
    LogFileName = "Marvellous_%s.log" % (timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    MyDict = FindDuplicate(DirectoryName)

    if MyDict == None:
        return

    fobj = open(LogFileName, "w")

    fobj.write("Starting Time : " + timestamp + "\n")
    fobj.write("Directory Scanned : " + DirectoryName + "\n\n")

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    for value in Result:

        for subvalue in value:

            Count = Count + 1

            if Count > 1:

                checksum = CalculateChecksum(subvalue)

                fobj.write("Deleted File : " + subvalue + "\n")
                fobj.write("Checksum : " + checksum + "\n\n")

                os.remove(subvalue)

                TotalDeleted = TotalDeleted + 1

        Count = 0

    fobj.write("Completion Time : " + time.ctime() + "\n")
    fobj.write("Duplicate Files Deleted : " + str(TotalDeleted) + "\n")
    fobj.write("Errors Encountered : None\n")
    fobj.write("Email Delivery Status : Not Sent\n")
    fobj.write("--------------------------------------------------------------------------")
    fobj.close()

    print("Total Deleted Files :", TotalDeleted)

# Email

def Marvellous_send_mail(sender, app_password, receiver, subject, body):

    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail App Password
    smtp.login(sender, app_password)

    # Step 6 : Send email
    smtp.send_message(msg)

    # Step 7 : Close connection
    smtp.quit()

# --------------------------------------------------
# Driver Code
# --------------------------------------------------
           
def main():

    # Always use a temporary/testing Gmail account
    sender_email = "vedashreemaharaj52@gmail.com"

    # Gmail App Password
    app_password = "xxxx xxxx xxxx xxxx"

    # Receiver Email
    receiver_email = "maharajvedashree2004@gmail.com"

    subject = "Test Mail from Python Script"

    body = """Jay Ganesh,

This is a test email sent using Marvellous Python.

Regards,
Marvellous Infosystems
"""

    Marvellous_send_mail(sender_email,
                         app_password,
                         receiver_email,
                         subject,
                         body)

    print("Marvellous Mail Sent Successfully")
    
    if len(sys.argv) != 3:
        print("Usage : python DuplicateFileRemoval.py DirectoryName TimeInMinutes")
        return

    Directory = sys.argv[1]
    Interval = int(sys.argv[2])

    schedule.every(Interval).minutes.do(DeleteDuplicate, Directory)

    print("Automation Started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

