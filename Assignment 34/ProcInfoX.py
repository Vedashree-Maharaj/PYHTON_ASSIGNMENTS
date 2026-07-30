# script which displays information of Display specific process as its name ,PID,Username

import psutil
import sys

def ProcessScan(ProcessName, FileName):
     fobj = open(FileName, "w")

     for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username"])

            if ProcessName.lower() in info["name"].lower():

                fobj.write("-"*40 + "\n")
                fobj.write("PID : %s\n" % info["pid"])
                fobj.write("Name : %s\n" % info["name"])
                fobj.write("Username : %s\n" % info["username"])

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

     fobj.close()

def main():
    if len(sys.argv) != 3:
        print("Usage : python ProcInfo.py ProcessName LogFileName")
        return

    ProcessScan(sys.argv[1], sys.argv[2])
    print("Log file created successfully.")

if __name__ == "__main__":
    main()