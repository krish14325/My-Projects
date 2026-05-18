class Library:
    
    def __init__(self):
        self.Customer_info={}
        self.book_ls = []
    def ADD_BOOK(self,book):
        self.book = book
        self.book_ls.append(self.book)
        print("Book Added Sucessfully....")
    def Issue_Book(self,name,book):
        self.name = name
        self.book = book
        if self.book in self.book_ls:
            self.book_ls.remove(self.book)
            self.Customer_info[name] = book
            print("Book Issued Sucessfully....")
        else:
            print("book is not available....")
    def Return_Book(self,name,book):
        self.name = name
        self.book = book
        if self.name in self.Customer_info:
            if self.Customer_info[name] == book:
                self.book_ls.append(self.book)
                self.Customer_info.pop(name)
                print("Book Returned Sucessfully....")
            else:
                print("Customer Does Not Exist")
    def viewbooks(self):
        print(self.book_ls)
obj = Library()
while True:
    print("1.Add Book\n2.Issue Book\n3.Return Book\n4.View Customers Info\n5.View Books\n6.Exit")
    Choice = input("Enter Option : ")
    if Choice == "1":
        bookname = input("Enter Book Name : ")
        obj.ADD_BOOK(bookname)
    elif Choice == "2":
        Customer = input("Enter Your Name : ")
        Book = input("Enter Your Book : ")
        obj.Issue_Book(Customer,Book)
    elif Choice == "3":
        Returner = input("Enter your name : ")
        book_return = input("Enter Book Name : ")
        obj.Return_Book(Returner,book_return)
    elif Choice == "4":
        print(obj.Customer_info)
    elif Choice == "5":
        obj.viewbooks()
    elif Choice == "6":
        break
    else:
        print("INVALID INPUT")
        
        
        