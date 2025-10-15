class BankAccount:

    def __init__(self, owener, balance):
        self.owener = owener
        self.__balance = balance

    def bygetter(self):
        return self.__balance

    def bysetter(self, amount):
        if amount>=0:
            self.__balance = amount
        else:
            print("Invalid amount!")


obj =BankAccount("seshadri",2200)

print(obj.bygetter())

obj.bysetter(54000)
print(obj.bygetter())
                 
