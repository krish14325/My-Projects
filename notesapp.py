class NotesApp:
    def write(self,text):
        self.text = text
        with open("practice.txt","a")as self.f:
            self.f.write(f"{text}\n")
            print("Text Added Sucessfully.....")
    def view(self):
        try:
            with open("practice.txt","r")as self.f:
                print(self.f.read())
                print("File Ended .....(This Text Was Not Included In File)")
        except FileNotFoundError:
            print("file not found")
    def clear(self):
        with open("practice.txt","w")as self.f:
            self.f.write("")
            print("File Cleared...")
obj1 = NotesApp()
while True:
    print("1.Add Notes\n2.View Notes\n3.Clear Notes\n4.Exit")
    choice = input("Enter Option : ")
    if choice == "1":
        text = input("Enter Text : ")
        obj1.write(text)
    elif choice == "2":
        obj1.view()
    elif choice == "3":
        obj1.clear()
    elif choice == "4":
        print("Exiting.....")
        break
    else:
        print('INVALID INPUT')
        
        
            
            
            
            
    