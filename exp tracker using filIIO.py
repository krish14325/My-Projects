while True:
    print("1.Save Expense\n2.Read Expense\n3.Exit")
    choice = input("Enter option : ")
    if choice == "1":
        Expense = input("Enter Expense : ")
        with open("practice.txt","a") as f:
            data = (f"{Expense}\n")
            f.write(data)
            print("Expense Added Sucessfully.....")
    elif choice == "2":
        try :
            with open("practice.txt","r") as f:
                if data == "":
                    print("no data found file is empty")
                else:
                    print(f.read())
        except FileNotFoundError:
            print("No File Exist...")
    elif choice == "3":
        print("Exiting....")
        break
    else:
        print("INVALID INPUT")
        
    

    
    
    




    