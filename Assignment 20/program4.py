# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# Small thread should count and display the number of lowercase characters.
# Capital thread should count and display the number of uppercase characters.
# Digits thread should count and display the number of numeric digits.
# Each thread should display its Thread ID and Thread Name.

import threading

def Small(String):
    Count = 0
    for ch in String:
        if ch.islower():
            Count += 1
    print("Small letters:", Count)

def Capital(String):
    Count = 0
    for ch in String:
        if ch.isupper():
            Count += 1
    print("Capital letters:", Count)

def Digits(String):
    Count = 0
    for ch in String:
        if ch.isdigit():
            Count += 1
    print("Digits:", Count)

def main():
    Str = input("Enter a string: ")

    t1 = threading.Thread(target=Small, args=(Str,), name="Thread1")
    t2 = threading.Thread(target=Capital, args=(Str,), name="Thread2")
    t3 = threading.Thread(target=Digits, args=(Str,), name="Thread3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()