class ContactBook:
    def __init__(self):
        self.contact_dict={}
    
    def add_contact(self,name,contact):
        self.name = name
        self.contact = contact
        self.contact_dict[name]= self.contact
        print("Contact Added Sucessfully....")
    
    def remove_contact(self,name):
        self.name = name
        self.contact_dict.pop(name)
        print("Contact Removed Sucessully....")
    
    def view_contacts(self):
        print(self.contact_dict)
        
contact = ContactBook()

while True:
    print("1.Add Contact\n2.Remove Contact\n3.View Contact\n4.Exit")
    Choice = input("Enter Option : ")
    if Choice == "1":
        number = int(input("Enter number : "))
        name = input("Enter name : ")
        name2 = name.lower()
        contact.add_contact(name2,number)
        
    elif Choice == "2":
        Name = input("Enter name : ")
        Name2 = Name.lower()
        if Name2 in contact.contact_dict:
            contact.contact_dict.pop(Name2)
            print("Contact Removed Sucessfully......")
        else:
            print("No Contact Existed By This Name")
            
    elif Choice == "3":
        contact.view_contacts()
        
    elif Choice == "4":
        break
    else:
        print("INVALID INPUT")
            
            
    
    