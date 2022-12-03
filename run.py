import colorama
colorama.init()

questions = {
    "What is the colour of Mace Windu's lightsaber?: ": "B",
    "Who or what killed Boba Fett?: ": "C",
    "Luke Skywalker's uncle and aunt are called Owen and...?: ": "C",
    "How many parsecs did Han Solo complete the Kessel Run?: ": "A",
    "What is the surface of the planet Crait covered with?: ": "A",
    "What is the name of the crystal used to create lightsabers?: ": "D",
    "Where does Yoda live when he first trains Luke Skywalker?: ": "B",
    "Which hand does Luke Skywalker lose?: ": "A",
    "What is Chewbacca’s weapon of choice?: ": "D",
    "What nickname does Han Solo call Luke Skywalker?: ": "C",
}

options = [["A. Blue", "B. Purple", "C. Green", "D. Yellow"],
           ["A. Darth Vader", "B. Han Solo", "C. Sarlacc", "D. Rancor"],
           ["A. Hana", "B. Nona", "C. Beru", "D. Leia"],
           ["A. 10", "B. 12", "C. 2", "D. 8"],
           ["A. Salt", "B. Snow", "C. Sand", "D. Soil"],
           ["A. Celestite", "B. Pyrite", "C. Opal", "D. Kyber"],
           ["A. Tatooine", "B. Dagobah", "C. Jakku", "D. Yavin"],
           ["A. Right", "B. Left", "C. Both", "D. Neither"],
           ["A. Blaster", "B. Lightsaber", "C. Club", "D. Bowcaster"],
           ["A. Buckaroo", "B. Skydancer", "C. Kid", "D. Lukie"]]


def start_game():
    """
    Function loops through question list and options list to 
    display question with corresponding option list in order.
    If answer is correct the score increseases by 1.
    """
    attempts = []
    correct_attempts = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(colorama.Fore.LIGHTYELLOW_EX + key)
        print(colorama.Fore.RESET)
        for i in options[question_num-1]:
            print(i)
        attempt = input("Answer: ")
        attempts.append(attempt)
        while attempt not in ('A', 'B', 'C', 'D',):
            attempt = input("Invalid attempt must choose from (A,B,C,D)\n")

        correct_attempts += check_answer(questions.get(key), attempt)
        question_num += 1

    display_score(correct_attempts, attempts)


def check_answer(answer, attempt):
    """
    Checks if the attmept is the same as the answer, if 
    its correct it prints thats right and returns 1 to the score, 
    if its wrong it prints thats wrong and returns 0 to the score.
    """
    if answer == attempt:
        print(colorama.Fore.GREEN + "Thats right!")
        print(colorama.Fore.RESET)
        return 1
    else:
        print(colorama.Fore.RED + "Thats wrong!")
        print(colorama.Fore.RESET)
        return 0


def display_score(correct_attempts, attempts):
    """
    Shows correct answers and users answers and calulates
    the score divides it by 10 and mulitplies by 100 to
    give a percentage. 
    """
    print("------------------------------")
    print("Your results are displayed below:")
    print("------------------------------")

    print("Correct answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your attempts: ", end="")
    for i in attempts:
        print(i, end=" ")
    print()
    print("------------------------------")

    print("If your score is 70% or more consider yourself one with the force.")
    score = int((correct_attempts/len(questions))*100)
    print("Score: "+str(score)+"%")


def play_again():
    """
    If user replies yes the new_game() will display,
    if user replies no message is printed. 
    """
    print("------------------------------")
    response = input("Do you want to play again? (YES or NO): ")

    while response not in {'YES', 'NO'}:
        response = input("Invalid input, try again\n")
    if response == "YES":
        return True
    else:
        return False


def main():
    """
    This functions runs all pograms when called at the 
    end of the code. 
    """
    print("")
    print("Do you consider yourself one with the force?")
    print("In this quiz, you will be aksed a total of 10 Questions.")
    print("This is a multiple choice quiz.")
    print("Your answers must be from options (A, B, C or D).")
    print("To move to the next question, pick your answer from the given")
    print("choices then hit the enter button.\n")
    start_game()
    while play_again():
        start_game()
    print("Goodbye and may the force be with you!")


main()