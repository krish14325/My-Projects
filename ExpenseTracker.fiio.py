class ExpenseTracker:
    def addexpense(self,expense,amount):
        with open("practice.txt","a+")as self.f:
            self.data = self.f.write(f"{expense} --> {amount}\n")
            print("Expense Added In Sucessfully.....")
    def viewexpense(self):
        try:
            with open("practice.txt","r") as self.f:
                print(self.f.read())
        except FileNotFoundError:
            print("File Not Found....")
            
    def showtotal(self):
        try:
            with open("practice.txt","r") as f:
                p=0
                for i in f:
                    n = i.strip().split(" --> ")
                    num = n[1]
                    p+= int(num)
                print(p)
        except FileNotFoundError:
            print("file not found")
obj1 = ExpenseTracker()
while True:
    print("1.Add Expense\n2.View Expense\n3.Show Total\n4.Exit")
    choice = input("Enter Option : ")
    if choice == "1":
        Expense = input("Enter Expense : ")
        Amount = int(input("Enter Amount : "))
        obj1.addexpense(Expense,Amount)
    elif choice == "2":
        obj1.viewexpense()
    elif choice == "3":
        obj1.showtotal()
    elif choice == "4":
        print("Exiting....")
        break
    else:
        print("INVALID INPUT")
            
        
        