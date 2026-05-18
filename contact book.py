Contact_book = {}
while True:
    print("1.Add Contact\n2.View Contact\n3.Delete Contact\n4.Exit")
    Choose = input("Enter Option Number : ")
    if Choose == "1":
        Number = int(input("Enter Number You Want To Add : "))
        Name = input("Enter Name You Want To Add : ")
        Contact_book[Name] = Number
    elif Choose == "2":
        if len(Contact_book)==0:
            print("no contacts exist")
        else:
          print(Contact_book)
    elif Choose == "3":
        number_delete = (input("Enter Name You Want To Delete : "))
        if number_delete in Contact_book:
            Contact_book.pop(number_delete)
    elif Choose == "4":
        print("Exiting....")
        break
    else:
        print("invalid input")
    
    
    
        
    
        
        
        
    
