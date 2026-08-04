import sys
import os
import time
import schedule
import psutil

def Process_id():
   list = []
   for proc in psutil.process_iter():
      info = proc.as_dict(attrs=["name","pid","username","status"])
      list.append(info)

   return list   

def FindProcess(FolderName, lc_folder):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory for the log file gets created.. ")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Filename = os.path.join(FolderName, f"Marvellous_{timestamp}.log")

    with open(Filename, "w") as fobj:
        print(f"Log file gets created with name {Filename}")

        rs = Process_id()
        if not rs:
            fobj.write(f"No process found from folder {lc_folder}\n")
        else:
            for data in rs:
                fobj.write(f"{data}\n")
                fobj.write("______________________________________________\n")

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This automation script fetches information of running processes.")
        elif sys.argv[1].lower() == "--u":
            print("Usage:")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name LC_Folder_Path")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name   : Name of folder for the log file creation")
            print("LC_Folder_Path: Path to LC folder containing executables")
    elif len(sys.argv) == 4:
        print("Scheduler started successfully...")
        print("Press Ctrl + C to abort the script")

        schedule.every(int(sys.argv[1])).minutes.do(FindProcess, sys.argv[2], sys.argv[3])

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u flag for help")

if __name__ == "__main__":
    main()