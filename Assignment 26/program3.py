# program to implement  a class named Arithmetic 

class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1 = int(input("Enter the First Number: "))
        self.Value2 = int(input("Enter the Second Number: "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self): 
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError:
            print("Exception occurred: Division by zero is not allowed.")
            return None
        

cobj = Arithmetic()

cobj.Accept()

print("Addition =", cobj.Addition())
print("Subtraction =", cobj.Subtraction()  )
print("Multiplication =", cobj.Multiplication())
Ans = cobj.Division()

if Ans is not None:
    print("Division =", Ans)