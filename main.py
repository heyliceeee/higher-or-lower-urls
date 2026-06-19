from flask import Flask
import random

random_number = random.randint(0, 9) # Generate a random number between 0 and 9
print(random_number) # Print the random number

app = Flask(__name__) # __name__ is a variable that contains the name of the module

@app.route("/")
def home():
    """
    Home page route
    :return: message
    """
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    """
    Guess a number route
    :param guess: number to guess
    :return: feedback
    """
    if guess > random_number: # if the guess is higher than the random number
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number: # if the guess is lower than the random number
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else: # if the guess is the same as the random number
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__": # if the file is run directly
    app.run(debug=True) # debug=True is for debugging
