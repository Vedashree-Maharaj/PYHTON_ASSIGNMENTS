# script to accept directory and in log file print pid username
import os
import time
import psutil
import sys
import smtplib
from email.message import EmailMessage
    

def PlatformSurvilence(FolderName):
    Border = "-"*50

    Ret = False

    Ret= os.path.exists(FolderName)

    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to Proceed as Directory name is existing but its not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created Successfully")

    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellos_%s.log" %timestamp) 

    fobj = open(FileName,"w")

    print(f"Log file gets successfully created with time {FileName}")

    fobj.write(Border+"\n")
    fobj.write("---- MARVELLOUS PLATFORM SURVILLRNCE SYSTEM ----\n")
    print(Border+"\n")
    fobj.write("Lof file gets created at:"+timestamp+"\n")
    fobj.write(Border+"\n")

    for proc in psutil.process_iter():
            try:
                info = proc.as_dict(attrs=["pid", "name", "username"])
    
                fobj.write(Border + "\n")
                fobj.write("PID : %s\n" % info["pid"])
                fobj.write("Name : %s\n" % info["name"])
                fobj.write("Username : %s\n" % info["username"])
    
            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass
    
    fobj.close()
    return FileName

def SendMail(FileName):

    sender = "vedashreemaharaj52@gmail.com"
    password = "rfhmfcbtjifiuewde"
    receiver = "maharajvedashree2004@gmail.com"

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Process Log File"

    msg.set_content("Please find the attached process log file.")

    fobj = open(FileName, "rb")
    FileData = fobj.read()
    fobj.close()

    msg.add_attachment(FileData,
                       maintype="application",
                       subtype="octet-stream",
                       filename=os.path.basename(FileName))

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(sender, password)

    smtp.send_message(msg)

    smtp.quit()

    print("Mail sent successfully.")

def main():
    Border="-"*50
    print(Border)
    print("---- MARVELLOUS PLATFORM SURVILLRNCE SYSTEM ----")
    print(Border)

# --h and --u handling
    if(len(sys.argv)==2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to perform :")
            print("1 : It fetch informtion of running processes")
            print("2 : It fetch informtion about the primary storage RAM")
            print("3 : It fetch informtion about the secondary storage as HDD ")
            print("4 : It fetch informtion about the microprocessor")
            print("5 : It gets auto-scheduled periodically")
            print("6 : It maintains all records in log file")
            print("7 : It sends log file to mail periodically")
            
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automations Script as :")
            print(f"python {sys.argv[0]}  Time_Interval Folder_Name ")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name for folder for the log file creation")

        else:
            print("Unable to process as Arguments are not matching")
            print("Please use --h or --u flag for getting more detail")
    
   
    else:
        print("Invalid Number of Arguments")
        print("Unable to process as Arguments are not matching")
        print("Please use --h or --u flag for getting more detail")


    print(Border)
    print("---- Thank You For Using our Automation System ----")
    print(Border)

    LogFile = PlatformSurvilence(sys.argv[1])

    SendMail(LogFile)
    

if __name__ == "__main__":
    main()
