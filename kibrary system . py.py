book_list = []
info_dict = {}
while True :
    print("..........Menu.........")
    print("1.Add Book\n2.Issue Book\n3.Return Book\n4.View Books\n5.View info\n6.Exit")
    Choose = input("Enter Option No. : ")
    if Choose == "1":
        Book_name = input("Enter Book Name : ")
        book_list.append(Book_name)
        print(".........Book Added Succesfully.........")
    elif Choose == "2":
        if len(book_list) == 0:
            print("No Books Available")
        else:
            Customer_name = input("Enter Customer Name : ")
            print("These books are currently available")
            for i in book_list:
                print(i)
            Issue_Book = input("Enter Book Name : ")
            info_dict[Customer_name] = Issue_Book
            if Issue_Book in book_list:
             book_list.remove(Issue_Book)
             print(".......BOOK ISSUED SUCCESFULLY........")
    elif Choose == "3":
        Returner = input("Enter your name : ")
        returning_book = input("Enter book name : ")
        if Returner in info_dict:
            del info_dict[Returner]    
        book_list.append(returning_book)  
        print(".......Book Returned........")  
    elif Choose == "4":
        print(book_list)
    elif Choose == "5":
        print(info_dict)
    elif Choose == "6":
        print("Exiting......")
        break
    else:
        print("invalid input")
        
        
            
    
    
        
        
    
    