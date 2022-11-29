def new_game():
    
    attempts = []
    correct_attempts = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        attempt = input("Answer: ")
        attempt = attempt.upper()
        attempts.append(attempt)

        correct_attempts += check_answer(questions.get(key), attempt)
        question_num += 1

    display_score(correct_attempts, attempts)


def check_answer(answer, attempt):

    if answer == attempt:
        print("Thats right!. The force is strong in you.")
        return 1
    else:
        print("Thats wrong!. Failed you have, into exile you just go.")
        return 0


def display_score(correct_attempts, attempts):
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

    print("If your score is 70% or more you are a hardcore fan. ")
    score = int((correct_attempts/len(questions))*100)
    print("Score: "+str(score)+"%")


def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "What is the colour of Mace Windu's lightsaber?: ": "B",
    "Who or what killed Boba Fett?: ": "C",
    "Luke Skywalker's uncle and aunt are called Owen and...?: ": "C",
    "How many parsecs did Han Solo complete the Kessel Run?: ": "A",
    "What is the surface of the planet Crait covered with?: ": "A",
    "What is the name of the crystal used to create lightsabers?: ": "D",
    "Where does Yoda live when he first trains Luke Skywalker?: ": "A",
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


new_game()