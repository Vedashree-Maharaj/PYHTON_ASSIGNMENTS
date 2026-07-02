#program which accept number and prints binary equivalent

def BinaryCheck(num):
  print(bin(num))
 

def main():
 number = int(input("Enter The Number:"))

 BinaryCheck(number)

 
if __name__ == "__main__":
  main()