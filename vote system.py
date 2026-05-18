competetors = {}
i = 0
n = 0
p = 0
while True:
    print("Choose your next PM")
    print("1.BJP\n2.Congress\n3.AAP")
    print("For Menu Press 5")
    print("...........................")
    Choose = input("Enter your Party : ")
    if Choose == "5":
        print("\n4.Show Full List\n7.Exit\n6.Show Winner")
    elif Choose == "1":
        i +=1
        competetors["BJP"]= i
        print("Vote Added Succesfully")
    elif Choose == "2":
        n +=1
        competetors["Congress"]= n
        print("Vote Added Succesfully")
    elif Choose == "3":
        p +=1
        competetors["AAP"]= p
        print("Vote Added Succesfully")
    elif Choose=="4":
        print(competetors)
    elif Choose =="6":
        print("The winner is ",max(competetors,key=competetors.get),"with",max(competetors.values()),"votes")
    elif Choose == "7":
        print("Exiting....")
        break
    else:
        print("INVALID INPUT")
    
        