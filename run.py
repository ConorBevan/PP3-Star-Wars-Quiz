def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        
        question_num += 1


def check_answer():
    pass


def display_score():
    pass


def play_again():
    pass


questions = {
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
    "Placeholder text?: ": "A",
}

options = [["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"],
           ["A. Placeholder text", "A. Placeholder text", "A. Placeholder text", "A. Placeholder text"]]


new_game()