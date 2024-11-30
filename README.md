# Craps Dice Game Website

Description
         This project is a web-based implementation of the popular dice game Craps using Python's Flask framework. The website allows players to roll virtual dice, calculate outcomes based on the rules of Craps, and enjoy a simple and interactive gaming experience.

Features
  Interactive Gameplay:
  Start a new game.
  Roll dice and see results dynamically.
  Visual indicators for wins and losses.
  
Responsive Design:
    Styled with CSS for an engaging user interface.
    Buttons and layout optimized for clarity and usability.

Simple Navigation:
    Homepage with game instructions.
    Game page displays dice rolls and game progress.
    
Rules of Craps
1.Roll two dice. Each die has faces numbered 1 to 6.
2.Calculate the sum of the numbers rolled:
   --> Win on the first roll if the sum is 7 or 11.
   --> Lose on the first roll if the sum is 2, 3, or 12 (called "craps").
   --> For any other sum (4, 5, 6, 8, 9, 10), that sum becomes the "point."
3. If a "point" is established:
    -->Continue rolling until you either:
        ==>Roll the "point" again (win).
        ==>Roll a 7 (lose).

Project structure
project/
│
├── app.py              # Flask application
├── templates/          # HTML templates
│   ├── home.html       # Homepage template
│   ├── game.html       # Game page template
├── static/             # Static files
    ├── styles.css      # CSS for styling

File Descriptions
1. app.py
    -->The main application file.
    -->Implements game logic and routes for:
        ==>/: Home page.
        ==>/start: Starts a new game and performs the first roll.
        ==>/roll: Rolls the dice in subsequent turns.

2. HTML Templates
    -->home.html: Displays the game instructions and a button to start playing.
    -->game.html: Shows dice rolls, game progress, and results.
3. CSS File
    -->styles.css: Adds styling to the website, including:
        ==>Background color and font settings.
        ==>Button hover effects.
        ==>Highlighted messages for winning and losing.

How It Works
1. Homepage:
    -->Displays instructions and a "Start Game" button.
2. Game Page:
    -->Shows dice rolls and calculates game status dynamically.
    -->Displays winning or losing messages.
    -->Allows players to roll again if the game continues.
Customization
    1. Styling: Modify styles.css to change the look and feel.
    2. Rules: Update app.py to adjust game rules or add new features.
    3. Features: Add score tracking, multiple players, or animations.

License
   This project is open-source and free to use. Contributions and improvements are welcome!

