while True:
    conversation = input("You: ")
    new_convo = (conversation.lower())
    n = "chatbot"
    if new_convo == "hello":
        print(n,":","hey!")
    elif new_convo == "how are you":
        print(n,":","i am fine")
    elif new_convo == "who are you":
        print(n,":","i'am jarvis")
    elif new_convo == "bye":
        print(n,":","bye")
        break
    else:
        print("invalid input")
    
