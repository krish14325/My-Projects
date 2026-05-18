class ATMMachine:
        def __init__(self):
            self.balance = 0
        try:
            def deposit(self,Money):
                self.balance+=Money
                print("AMOUNT DEPOSITED SUCESSFULLY")
        except ValueError:
            print("Value Error")
        try:
            def withdraw(self,Amount):
                self.balance -= Amount
                print("AMOUNT CREDITED SUCESSFULLY")
        except ValueError:
            print("Value Error")
        def show(self):
            print("YOUR TOTAL BALANCE WAS -- > ",self.balance)
obj1 = ATMMachine()
while True:
    print("1.Deposit Money\n2.Withdraw Money\n3.Check Balance\n4.Exit")
    Choice = input('Enter Option : ')
    if Choice == "1":
        Deposit = int(input("Enter Amount To Deposit : "))
        obj1.deposit(Deposit)
    elif Choice == "2":
        Credit = int(input("Enter Amount To Withdraw : "))
        obj1.withdraw(Credit)
    elif Choice == "3":
        obj1.show()
    elif Choice == "4":
        print("Exiting....")
        break
    
            
            
        
        
    
