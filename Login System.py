class System():
    def register(self,name,password):
        with open("practice.txt","a") as f:
            f.write(f"{name} --> {password}\n")
            print("User Register Sucessfully.....")
    def login(self,Name,Password):
        try:
            with open("practice.txt","r")as f:
                lines = f.readlines()
                for i in lines:
                    stored_name , stored_pass = i.strip().split(" --> ")
                    if stored_name == Name and stored_pass == Password:
                        print("Login Sucessfully")
                        return
                print("USER NOT FOUND")
        except FileNotFoundError:
            print("FILE NOT FOUND")
obj1 = System()
while True:
    print("1.Register User\n2.Login User\n3.Exit")
    choice = input("Enter option : ")
    if choice == "1":
        name = input("Enter Name : ")
        Password = input("Enter Password : ")
        obj1.register(name,Password)
    elif choice == "2":
        Name = input("Enter Name : ")
        password = input("Enter Password : ")
        obj1.login(Name,password)
    elif choice == "3":
        print("Exiting....")
        break
    else:
        print("INVALID INPUT")
                      
                        