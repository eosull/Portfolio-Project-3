# Battleship Game

## Python Portfolio Project 3

![Image of game title](assets/readme-images/title-screenshot.png)

![Image of gameplay](assets/readme-images/gameplay-screenshot.png)

## Introduction
This battleship game was developed for Portfolio Project 3 - Python Essentials. It is designed to 
be played within the Code Institute mock terminal hosted on Heroku - [Link to game](https://portfolio-project-3-battleship.herokuapp.com/)

The aim of the game is to sink all of your opponents ships before they sink yours. In this case
the user plays agains the computer. It is based on the classic battleship board game, rules for
this can be found [here](https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm)

Using a command-line interface, the user can select rows and columns to guess where the computer's
ships are positioned. Each time the user makes a guess the board is updated and the user is informed
of whether they scored a hit or a miss. This continues until either the user or the computer sinks
all of their opponents ships and therefore win the game.

## User Experience & Game Goals
- The aim as a developer was:
  - To build an easy to play game that was enjoyable
  - To allow the user to select their own difficulty

- As a user I want to:
  - Understand the rules of the game
  - Consistent feedback on input and right/wrong guesses
  - Emjoy the game
  - Increase or decrease the difficulty if I want to play again

## Design

## Features

## Technologies Used

## Testing

## Deployment

## Forking/Cloning Project

## Credits





## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!