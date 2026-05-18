class ContactBook:
    def addcontact(self, name, contact):
        with open("contacts.txt", "a") as f:
            f.write(f"{name} : {contact}\n")
            print("Contact Added Successfully....")

    def viewcontact(self):
        try:
            with open("contacts.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("FILE NOT FOUND")

    def searchcontact(self, name):
        try:
            with open("contacts.txt", "r") as f:
                for line in f:
                    if name.lower() in line.lower():
                        print("Contact Found.....")
                        print(line)
                        return
            print("Contact Not Found ❌")
        except FileNotFoundError:
            print("FILE NOT FOUND")


obj1 = ContactBook()

while True:
    print("1.Add Contact\n2.View Contact\n3.Search Contact\n4.Exit")
    choice = input("Enter Option : ")

    if choice == "1":
        name = input("Enter Name : ")
        contact = input("Enter Contact : ")
        obj1.addcontact(name, contact)

    elif choice == "2":
        obj1.viewcontact()

    elif choice == "3":
        name = input("Enter Name : ")
        obj1.searchcontact(name)

    elif choice == "4":
        print("Exiting")
        break

    else:
        print("INVALID INPUT")