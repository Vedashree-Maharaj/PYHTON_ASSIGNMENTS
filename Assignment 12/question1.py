# Program to accept a character and check vowel or not

def Vowel(char1):
    lis = ["a", "e", "i", "o", "u"]

    for ch in lis:
        if char1 == ch:
            return True

    return False

def main():
    Char2 = input("Enter the character: ")

    Ret = Vowel(Char2)

    if Ret == True:
        print("The given character is Vowel")
    else:
        print("The character is not a Vowel")

if __name__ == "__main__":
    main()