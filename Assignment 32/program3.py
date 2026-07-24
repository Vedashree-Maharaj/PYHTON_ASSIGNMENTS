# program that readsand displays the content of specified text file every minute

import os
import time
import schedule

def ReadFile(FileName):
    try:
        
        if not os.path.exists(FileName):
            print("Error: File does not exist.")
            return

        if os.path.getsize(FileName) == 0:
            print("Error: File is empty.")
            return

       
        fobj = open(FileName, "r")

        print("\n----- File Contents -----")
        print(fobj.read())
        print("-------------------------")

        fobj.close()

    except FileNotFoundError:
        print("Error: File does not exist.")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError:
        print("Error: File cannot be opened.")

    except Exception as e:
        print("Unexpected Error:", e)


def main():
    FileName = input("Enter file name: ")

    schedule.every(1).minutes.do(ReadFile, FileName)

    print("Reading file every minute...")

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()