from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Global variables to track game status
game_status = None
my_point = None

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)

@app.route("/")
def home():
    """Display the home page with game instructions."""
    return render_template("home.html")

@app.route("/start")
def start_game():
    """Start a new game and determine the result of the first roll."""
    global game_status, my_point
    dice = roll_dice()
    sum_of_dice = sum(dice)

    # Determine game status based on first roll
    if sum_of_dice in (7, 11):  # Win
        game_status = "WON"
    elif sum_of_dice in (2, 3, 12):  # Lose
        game_status = "LOSE"
    else:  # Continue playing
        game_status = "CONTINUE"
        my_point = sum_of_dice

    return render_template("game.html", dice=dice, sum_of_dice=sum_of_dice, game_status=game_status, my_point=my_point)

@app.route("/roll")
def roll_again():
    """Roll the dice if the game is continuing."""
    global game_status, my_point
    if game_status != "CONTINUE":
        return redirect(url_for("start_game"))

    dice = roll_dice()
    sum_of_dice = sum(dice)

    # Determine game outcome
    if sum_of_dice == my_point:  # Win
        game_status = "WON"
    elif sum_of_dice == 7:  # Lose
        game_status = "LOSE"

    return render_template("game.html", dice=dice, sum_of_dice=sum_of_dice, game_status=game_status, my_point=my_point)

if __name__ == "__main__":
    app.run(debug=True)
