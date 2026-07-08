# program to display first 10 even numbers on screen
def Even():
    for i in range(2, 21):
        if i % 2==0:
            print(i,end="  ") 

def main():
   Even()

if __name__ == "__main__":
    main()


"""
OR
def Even():
    for i in range(2, 21, 2):
        print(i,end="  ")

def main():
    Even()

if __name__ == "__main__":
    main()


"""