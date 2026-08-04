import sys
import os
import time
import schedule
import psutil
import smtplib
from email.message import EmailMessage

def Process_id():
    process_list = []
    for proc in psutil.process_iter(attrs=["name","pid","username","status"]):
        process_list.append(proc.info)
    return process_list

def send_mail(sender, app_password, receiver, subject, body, attachment_path=None):
    
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    # attach log file if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="plain",
                filename=os.path.basename(attachment_path)
            )

    # create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

def FindProcess(FolderName,receiver_email):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory for the log file gets created.. ")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Filename = os.path.join(FolderName, f"Marvellous_{timestamp}.log")

    fobj = open(Filename, "w")
    print(f"Log file gets created with name {Filename}")

    rs = Process_id()
    if not rs:
            fobj.write("No processes found\n")
            body = "Jay Ganesh,\n\nNo processes found.\n\nRegards,\nVaibhav Kulkarni"
    else:        
            body_lines = ["Jay Ganesh,", "", "Here are the running processes:"]
            for data in rs:
                fobj.write(f"{data}\n")
                fobj.write("______________________________________________\n")
                body_lines.append(str(data))
            body_lines.append("")
            body_lines.append("Regards,")
            body_lines.append("Vedashree Maharaj")
            body = "\n".join(body_lines)

    # Email details
    sender_email = "maharajvedashree2004@gmail.com"
    app_password = "rfhm fcbt jfiu ewde"   # <-- replace with real Gmail App Password
    subject = "Process Log Report"
    fobj.close()

    send_mail(sender_email, app_password, receiver_email, subject, body, Filename)
    print("Mail sent successfully..")

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This automation script fetches information of running processes.")
        elif sys.argv[1].lower() == "--u":
            print("Usage:")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name LC_Folder_Path")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name   : Name of folder for the log file creation")
            print("Recivers email")
    elif len(sys.argv) == 4:
        print("Scheduler started successfully...")
        print("Press Ctrl + C to abort the script")

        schedule.every(int(sys.argv[1])).seconds.do(FindProcess, sys.argv[2], sys.argv[3])
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u flag for help")

if __name__ == "__main__":
    main()