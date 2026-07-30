# script which displays information of running processes as its name ,PID,Username

import psutil
import sys

def ProcessScan(FileName):
    fobj = open(FileName, "w")

    Border = "-" * 50

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

def main():
    if len(sys.argv) != 2:
        print("Usage : python ProcInfo.py LogFileName")
        return

    ProcessScan(sys.argv[1])
    print("Log file created successfully.")

if __name__ == "__main__":
    main()