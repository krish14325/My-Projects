def calculator():
    while True:
        a = int(input("enter number : ")) 
        b = int(input("enter number : "))
        operation = input("Enter operator")
        if operation == "+":
                print(a + b)
        elif operation == "-":
            print(a - b)
        elif operation == "*":
            print(a * b)
        elif operation == "/":
            print(a / b)
        else:
            print("invalid input")
        while True :
            again = input("do you want to continue (YES/NO): ")
            if again == "yes" or  again == "YES":
                break
            elif again == "no" or again == "NO":
                return
            else:
                print("invalid input")
calculator()
        
    
    

   

        
        
    
    


