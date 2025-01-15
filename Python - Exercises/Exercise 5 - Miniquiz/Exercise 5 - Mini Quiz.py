import threading
import time
import sys
import random



class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

# Prompt user for details
def main():
    print("Welcome to Quiz.io!")
    
    user_id = input("Please input your name:    ")

    while True:
        ready = input("Are you ready to begin the quiz? (YES/EXIT)  ").strip().upper()

        if ready == "YES":
            game(user_id)
            break
        elif ready == "EXIT":
            break
        else:
            print("Invalid input. Please enter 'Yes' when you are ready to enter the game.")

# Initialize game
def game(user_id):
    
    #Initialize questions and scorecard
    question_list = load_questions()
    score = 0
    max_score = 5
    

    
    #Generate questions and check
    print("\n ***Lets begin!*** \n")
    for q in question_list:
        print(q.question)
        print(q.choices)
        print("You have 15 seconds to answer each question!")
        
        #Initialize timer duration

        timer_thread = threading.Thread(target=timer, args=(15,))
        timer_thread.start()
        timer_event = threading.Event()
        
        user_input = input("Please enter your answer (A/B/C):   ")
        
        while not timer_event.is_set():
            if user_input == q.answer:
                print("Well done! +1")
                score += 1
            else:
                print(f"You got it wrong :( The answer was  {q.answer}")
        if timer_event.is_set():
            print("Time's up! Moving to the next question.")



    #Display results
    print(f"Thank you for taking the quiz, {user_id}! Your score was {score} out of {max_score}") 
    if score < 5:
        print("You'll do better next time!")
    else:
        print("Well done, you got everything right  :)") 
    
def timer(t, timer_event):
    
    while t > 0:
        time.sleep(1)
        t -= 1
        if t == 10:
            print(f"{t} seconds left!", flush=True)
            sys.stdout.flush()

    timer_event.set()
    
    return True
        
#validate answer(user_input, q):

def load_questions():
    
    Q1 = Question("Who is the CEO of Meta?",
            ["A. Elon Musk", "B. Mark Zuckerberg", "C. Bill Gates"],
            "B")

    Q2 = Question("How many continents are there in the world?", ["A. 5", "B. 6", "C. 7"], "C")

    Q3 = Question("How many planets are there in the solar system?", 
            ["A. 7", "B. 8", "C. 9", "D. 10"],
            "B")

    Q4 = Question("Who discovered the Theory of Relativity?", 
            ["A. Nils Bohr", "B. Stephen Hawking", "C. Albert Einstein", "D. Edwin Hubble"],
            "C")

    Q5 = Question("What was the largest empire in history by land-mass?", 
            ["A. Mongol Empire", "B. Soviet Union", "C. British Empire", "D. Qing Dynasty"],
            "C")
    
    #Generated randomized order of questions    
    question_list = [Q1, Q2, Q3, Q4, Q5]
    random.shuffle(question_list)
        
    return question_list

if __name__ == "__main__":
    main()