import random
secret = random.randint(1,100)
while True:
    user_guess = int(input("enter number : "))
    if user_guess == secret:
        print("Congratulations you won 😍")
        break
    elif user_guess > secret:
        print("TOO HIGH")
    else :
        print("TOO LOW")
        
    
        

    
        
    
    

   

        
        
    
    


