expenses = []
balance = []
while True:
    print("1.Add Expenses\n2.View Expenses\n3.Delete Expenses\n4.View Total\n5.Exit")
    choose = int(input("Enter Number : "))
    if choose == 1:
        Expense = input("Enter Expense : ")
        amount = int(input("Enter Amount :"))
        expenses.append(Expense)
        balance.append(amount)
        print("Expenses Added Succesfully")
    elif choose == 2:
        print("here is the list of your expenses")
        for i in range(len(expenses)):
            print(i+1,"->",expenses[i], "of", balance[i],"Rs")
    elif choose == 3:
        value = int(input("Enter number of expense : "))
        if value > len(expenses) or value <= 0:
            print("invalid input")
        else:
            index = (value - 1)
            delete = expenses.pop(index)
            delete2 = balance.pop(index)
            print("item deleted succesfully")
        
    elif choose == 4:
        sum = 0
        for i in balance:
            sum+= i
        print("your total amount for total items was",sum,"Rs")
    elif choose == 5:
        print("Exiting...")
        break
    else:
        print("INVALID INPUT")
    
        