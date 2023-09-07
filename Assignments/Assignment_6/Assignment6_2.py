class BankAccount:
    ROI = 10.5
    
    def __init__(self,Name,Amount):
        self.name = Name
        self.amount = Amount
        
    def Display(self):
        print("Hello ",self.name)
        print("Your Balance is : ",self.amount)
        
    def Deposit(self,Amount):
        self.amount = self.amount + Amount
        print("Amount Deposited Successfully...")
    
    def WithDraw(self,Amount):
        if self.amount < Amount:
            print("There is no sufficient Amount")
        else:
            self.amount = self.amount-Amount
            print("Amount widrawal succeessfully...")
            
    def CalculateInterest(self,time):
        interest = (self.amount * self.ROI * time) / 100
        self.amount += interest
    
def main():
    print("ROI Of HDFC bank is",BankAccount.ROI)
    
    print("Creating new account...")
    
    Value1 = input("Enter Name : ")
    Value2 = int(input("Enter Amount : "))
    
    obj1 = BankAccount(Value1,Value2)

    obj1.Display()
    
    Value2 = int(input("Enter Widrwal Amount : "))
    
    obj1.WithDraw(Value2)
    
    obj1.Display()
    
    Value2 = int(input("Enter Deposit Amount : "))
    
    obj1.Deposit(Value2)
    
    obj1.Display()
    
    print("Intrest Of bank: ")
    
    obj1.CalculateInterest(2)
    
    obj1.Display()
    
    print("Creating new account...")
    
    Value1 = input("Enter Name : ")
    Value2 = int(input("Enter Amount : "))
    
    obj2 = BankAccount(Value1,Value2)

    obj2.Display()
    
    print("Performing Operation On Second Account : ")
    
    Value = int(input("Enter Widrwal Amount : "))
    
    obj2.WithDraw(Value)
    
    obj2.Display()
    
    Value = int(input("Enter Deposit Amount : "))
    
    obj2.Deposit(Value)
    
    obj2.Display()
    
    print("Intrest Of bank: ")
    
    obj2.CalculateInterest(3)
    
    obj2.Display()
    
if __name__ == "__main__":
    main()