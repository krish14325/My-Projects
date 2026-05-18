class Bank:
    def __init__(self):
        self.account = {}
    def create(self,name,password):
        if name in self.account:
            print("Account already existed...")
        else:
            self.account[name] = {"password" : password , "balance" : 0}
            print("Account Created Sucessfully...")
    def login(self,name,password):
            if name in self.account and self.account[name]["password"]==password:
                print("Login in sucessfull")
                self.menu(name)
            else:
                print("User Input Invalid")
    def menu(self,name):
        while True:
            print("1.Deposit Money\n2.Withdraw Money\n3.Show Balance\n4.All Accounts\n5.Exit")
            Choose = input("Enter Option : ")
            if Choose=="1":
                amount = int(input("Enter Amount : "))
                self.deposit(name,amount)
            elif Choose == "2":
                Amount = int(input("Enter Amount : "))
                self.Withdraw(name,Amount)
            elif Choose == "3":
                self.show(name)
            elif Choose == "4":
                self.accounts()
            elif Choose == "5":
                print("Exiting....")
                break
            else:
                print("INVALID INPUT")
    def deposit(self,name,amount):
        self.account[name]["balance"]+= amount
        print("Amount Deposited..")
    def Withdraw(self,name,amount):
        if amount>  self.account[name]["balance"] and amount <=0:
            print("Insufficient Balance")
        else:
            self.account[name]["balance"]-= amount
            print("Amount credited Sucessfully")
    def show(self,name):
        print(self.account[name]["balance"])
    def accounts(self):
        print(self.account)
obj1 = Bank()
while True:
    print("1.Create Account\n2.Login\n3.Exit")
    Choice = input("Enter Option : ")
    if Choice == "1":
        Name = input("Enter Name : ")
        Password = input("Create Password : ")
        obj1.create(Name,Password)
    elif Choice =="2":
        name = input("Enter Name : ")
        password = input("Enter Password : ")
        obj1.login(name,password) 
    elif Choice == "3":
        print("Exiting...")
        break
    else:
        print("INVALID INPUT")
        
        