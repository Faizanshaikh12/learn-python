questions = {
    "Who created Python? ": "A",
    "What year was Python created? ": "B",
        "Python is tributed to which comedy group? ": "C",
            "Is the Earth round? ": "A",
}

options = [
    ["A. Guido van Rossum", "B. James Gosling", "C. Larry Wall", "D. Elon Musk"],
    ["A. 1989", "B. 1991", "C. 1995", "D. 2000"],
    ["A. Monty Python", "B. The Three Stooges", "C. The Marx Brothers", "D. The Simpsons"],
    ["A. Yes", "B. No", "C. Sometimes", "D. What's Earth?"]
]

def new_game():
    guesses = []
    correct_gusses = 0
    question_num = 1

    for key in questions:
        print('--------------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_gusses += check_answer(questions.get(key), guess)
        question_num +=1
    
    display_score(correct_gusses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        return 1
    else:
        return 0

def display_score(correct_gusses, guesses):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = correct_gusses/len(questions)*100
    print("Score: ", score, "%")
    
def play_again():
    response = input(f"Do you want to play again? Enter 'yes' or 'no': ").upper()
    if response == "YES":
        return True
    else:
        return False