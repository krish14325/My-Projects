class Quiz:
    def __init__(self):
        self.questions = {
            "What is the Capital of India" : "delhi",
            "Who is PM Of India" : "modi",
            "What Is The Colour Of Rose" : "red",
        }  
    def start(self):
        self.score = 0
        for i in self.questions:
            print(i)
            while True:
                self.answer = input("Enter Answer : ")
                self.answer2 = self.answer.lower()
                if self.answer2 == self.questions[i]:
                    self.score+=1
                    print("YES IT IS CORRECT ANSWER",self.score)
                    break
                else:
                    print("try again")  
obj = Quiz()
while True:
    print("1.Start Quiz\n2.Stop Quiz")
    Choice = input("Enter Option : ")
    if Choice == "1":
        obj.start()
    elif Choice == "2":
        print("Your Total Score Was",obj.score)
        break
    else:
        print("INVALID INPUT")
            
        