# Program to implement a class BookStore

class BookStore:
    NoOfBook=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoOfBook=BookStore.NoOfBook + 1

    def Display(self):
        print(f"{self.Name} by {self.Author} . No of Books : {self.NoOfBook}")

cobj1=BookStore("Linux System Programming","Robert Love")
cobj1.Display()

cobj2=BookStore("C Programming","Dennis Ritchie")
cobj2.Display()