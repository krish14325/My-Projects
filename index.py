class Hotel:
    rooms = []
    AVAILABLE_ROOMS = ["AC ROOM" , "NON-AC ROOM" , "NORMAL ROOM"]
    def book_room(self,room):
        if room in self.AVAILABLE_ROOMS:
            self.rooms.append(room)
            self.AVAILABLE_ROOMS.remove(room)
            print("ROOM Booked Sucessfully")
        else:
            print("No Room Found")
    def Cancel(self , cancel):
        try:
            if cancel in self.rooms:
                self.rooms.remove(cancel)
                self.AVAILABLE_ROOMS.append(cancel)
                print("Room Canceled")
            else:
                print("ROOM Does Not Booked")
        except ValueError:
            print("No Room Found")
    def available(self):
        print(f"{self.AVAILABLE_ROOMS}")
        print("THESE ROOMS ARE AVAILABLE")
    def records(self):
        if len(self.rooms) == 0:
            print("NO ROOMS ARE BOOKED")
        else:
            print(f"{self.rooms}")
            print("THESE ROOMS ARE BOOKED")
obj1 = Hotel()
while True:
    print("1.book room\n2.cancel booking\n3.check rooms\n4.records\n5.Exit")
    choice = input("Enter option : ")
    if choice == "1":
       obj1.available()
       room = input("Enter Room : ").upper()
       obj1.book_room(room)
    elif choice == "2":
        cancel = input("Enter Room : ").upper()
        obj1.Cancel(cancel)
    elif choice == "3":
        obj1.available()
    elif choice =="4":
        obj1.records()
    elif choice == "5":
        print("Exiting....")
        break
    else:
        print("INVALID INPUT")
        
        
       
       
        
    
                
                
                
            
            
    
        
        

            
            
            
            