to_do_list =[]
while True:
    print("1. ADD TASK \n2. VIEW TASK \n3. DELETE TASK \n4.EXIT")
    user_choose = input("what do you want to choose between these options (1-4) : ")
    if user_choose == "1":
        task = input("enter your Goal/ Task : ")
        to_do_list.append(task)
        print("Task added")
    elif user_choose == "2":
        if len(to_do_list) == 0:
            print("your list is empty")
        else:
            print("Here is Your bucket list :")
            n = 1
            for i in to_do_list:
                print(n, "->", i)
                n+=1
            print("you have total",len(to_do_list),"tasks")
    elif user_choose == "3":
        goal = int(input("Enter goal number : "))
        if goal == 0 or goal < 0 or goal > len(to_do_list): 
            print("invalid input")
        else:
            index = goal - 1
            to_do_list.pop(index)
            print("your to_do_list was cleared ")
    elif user_choose == "4":
        print("Thanks for using our to_do_list program")
        break
        
        
    
        

    
        
    
    

   

        
        
    
    


