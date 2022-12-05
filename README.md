# Star Wars Quiz

Star Wars Quiz is a Pyhton terminal game, which runs in the Code Institute mock terminal on Heroku. The terminals main purpose is for users to test their Star Wars knowledge. Anyone can take the quiz. 

![Responsice Mockup](docs/)

## How to Play

The user will need to reply yes or no to strat the quiz.

There is 10 questions to answer with the options (A, B, C, D).

Users will be given a score at the end of the quiz.

You can play again when prompted by replying YES or NO.

## Features

### Intro Screen:

- This sstart section is used to explian the rules to the user about to take the Quiz.

![Intro Screen](docs/Screenshot1.png) 

### Quiz Questions:

- Each question is highlighted in yellow to stand out to the user.
- To answer the question you must input (A,B,C,D).
- If you get it right a message is printed,same if you get one wrong.
- if you put in a invlaid inout a message is prompted and you get to type another answer.

![Quiz Questions](docs/Screenshot2.png)

### Score:

- The correct answers are displayed.
- Your score is displayed which is calcutaled by each correct attempts which equals 1 divided by the length of questions (10) and multiplied by 100 with a string at the end to make it look like a percenatge score. 

![Score](docs/Screenshot3.png)

### Play Again Input:

- Here you have the option to play the quiz again but inputting YES. 
- If you answer NO, a message is printed and game ends. 

![Play Agian Input](docs/Screenshot4.png)

### Future Features

  - I would like to double the amount of available questions and make it so a random 10 questions are shown. 

## Data Models

I used a dictionary to store my data for my quiz questions and a list of lists to store the corresponding answers.

![Data Models](docs/Screenshot5.png)

## Testing 

### Validator Testing

I have manually tested this project by doing the following:

- Python - No errors were found when passing through the official [(PEP8) linter](https://pep8ci.herokuapp.com/).

![PEP8](docs/Screenshot6.png)

- Tested in my local terminal and the Code Institute heroku terminal. 

### Bugs

At first I didnt have the correct input validation and if you put a lowercase (a,b,c,d) and then put the correct input of (A,B,C,D) it would still co e up as correct. So i chnaged ti that you must answer in capitla letters to avoid this from happening. Otherwise I have had no other bug issues. 

# Deployment 

The live link can be found here - 

- Fork or clone this repository 
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in that order
- Link the Heroku app to the repository 
- Click on Deploy 

# Credits 

- This websiute and the courde content was used for my database -  (https://realpython.com/python-quiz-application/)
- Colorama was used to add some color to my code in terminal - (https://pypi.org/project/colorama/)
- This video was used to show how to use colorama properly - (https://www.youtube.com/watch?v=u51Zjlnui4Y)