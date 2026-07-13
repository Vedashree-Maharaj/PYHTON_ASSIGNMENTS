# Program to implement a class BankAccount

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self):
        Amount_Deposit = int(input("Enter the amount to deposit: "))
        self.Amount = self.Amount + Amount_Deposit

    def Withdraw(self):
        Amount_Withdraw = int(input("Enter the amount to withdraw: "))

        if self.Amount >= Amount_Withdraw:
            self.Amount = self.Amount - Amount_Withdraw
        else:
            print("Insufficient Balance")

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():
    cobj = BankAccount("abc", 10000)

    cobj.Display()

    cobj.Deposit()
    cobj.Display()

    cobj.Withdraw()
    cobj.Display()

    print("Interest =", cobj.CalculateInterest())


if __name__ == "__main__":
    main()