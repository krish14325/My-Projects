class Expense:
    def __init__(self):
        self.expenses = {}

    def addexpense(self,expense,cost):
        self.ExpensE = expense
        self.cost = cost
        self.expenses[expense]=cost
        print("Expense Added Sucessfully...")
    def deletexpense(self,expense):
        self.expenses.pop(expense)
        print("Expense Removed Sucessfully....")
    def show_total(self):
        for i in self.expenses.values():
            total = sum(self.expenses.values())
        print("Your Total Amount for Expenses was : ",total)
        
    def highest(self):
        if len(self.expenses) == 0:
            print("No expenses available")
        else:
            highest_exp = max(self.expenses, key=self.expenses.get)
            print("Highest expense:", highest_exp, "->", self.expenses[highest_exp], "Rs")

obj1 = Expense()
while True:
    print("1.Add Expense\n2.Remove Expense\n3.Show Total\n4.Show Highest\n5.Exit")
    Choice = input("Enter Option : ")
    if Choice == "1":
        exp = input(" Enter Expense Name : ") 
        cost = int(input("Enter Cost : "))
        obj1.addexpense(exp,cost)
    elif Choice == "2":
        namexp = input("Enter expense to delete : ")
        if namexp in obj1.expenses:
            obj1.deletexpense(namexp)
    elif Choice == "3":
        print(obj1.show_total())
    elif Choice == "4":
        obj1.highest()
    elif Choice =="5":
        print("Exiting....")
        break
        
    