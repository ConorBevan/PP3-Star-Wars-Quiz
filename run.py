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