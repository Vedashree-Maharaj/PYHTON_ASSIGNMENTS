# Program to implement a class named Numbers

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


def main():
    obj1 = Numbers()

    if obj1.ChkPrime():
        print(obj1.Value, "is a Prime Number")
    else:
        print(obj1.Value, "is not a Prime Number")

    if obj1.ChkPerfect():
        print(obj1.Value, "is a Perfect Number")
    else:
        print(obj1.Value, "is not a Perfect Number")

    obj1.Factors()

    print("Sum of Factors =", obj1.SumFactors())


if __name__ == "__main__":
    main()