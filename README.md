# Python Simple Projects

A collection of beginner-friendly Python programs created during the Code Labs Python session.

## Overview

This repository contains simple yet practical Python applications designed to help learners understand fundamental programming concepts including control flow, data structures, functions, object-oriented programming, and GUI development. Each program demonstrates core Python features through interactive examples.

## What's Included

### Games
- **GuessNumber.py** - A number guessing game with 3 attempts to find the randomly generated number
- **Hangman.py** - Word guessing game where players have 6 attempts to guess letters in a hidden word
- **RockPaperScissors.py** - Classic game against the computer with score tracking
- **TicTacToe.py** - Two-player game with graphical interface using tkinter
- **SnakeGame.py** - Traditional snake game with GUI implementation

### Utilities
- **Calculator.py** - Basic calculator supporting addition, subtraction, multiplication, and division
- **Password_generator.py** - Generates secure random passwords of specified length
- **Dice_roll.py** - Virtual dice roller simulator
- **Link_shortner.py** - URL shortening tool using the TinyURL API
- **TodoList.py** - Task management application with add, view, complete, and delete operations

## Use Cases

**Learning & Education**
- Introduction to Python syntax and control structures
- Understanding loops, conditionals, and functions
- Learning GUI programming with tkinter
- Practice with user input and data validation

**Beginner Portfolio Projects**
- Showcase foundational programming skills
- Demonstrate ability to create functional applications
- Build confidence through complete, working programs

**Quick Utilities**
- Standalone tools for daily tasks
- Foundation to extend with additional features
- Examples for implementing similar functionality

## Requirements

Most programs require only Python 3.6+. Two programs require additional libraries:

- **Link_shortner.py**: `pyshorteners` library
  ```bash
  pip install pyshorteners
  ```

- **TicTacToe.py** and **SnakeGame.py**: tkinter (included with Python on most systems)

## How to Run

Each program is standalone and can be executed directly:

```bash
python Calculator.py
python GuessNumber.py
python RockPaperScissors.py
```

Programs use interactive command-line interfaces or GUI windows depending on their nature.

## Program Descriptions

### Calculator.py
A multi-operation calculator that supports basic arithmetic. Users select operations through a menu and enter two numbers to perform calculations. Includes error handling for division by zero and invalid inputs.

### GuessNumber.py
Generates a random number between 1-10 and gives players three attempts to guess it. Provides feedback on each guess and reveals the correct number at the end.

### Hangman.py
Players guess letters to reveal a hidden word within 6 attempts. Tracks correctly guessed letters and remaining attempts. Ends when the word is guessed or attempts are exhausted.

### RockPaperScissors.py
Interactive game against computer opponent with persistent score tracking across multiple rounds. Computer makes random selections while players input their choice each turn.

### TodoList.py
Simple task management system allowing users to add, view, mark complete, and delete tasks. Displays task status with visual indicators.

### Password_generator.py
Creates random passwords combining lowercase, uppercase, digits, and special characters. Users specify desired password length.

### Dice_roll.py
Simulates rolling a six-sided die with results ranging from 0-6. Users can roll multiple times within a single session.

### Link_shortner.py
Converts long URLs into short, shareable links using the TinyURL API. Requires internet connection and pyshorteners library.

### SnakeGame.py
GUI-based snake game where players control a snake to eat food and grow longer. Includes collision detection and score tracking.

### TicTacToe.py
Two-player tic-tac-toe with GUI interface. Features winning detection for rows, columns, and diagonals, along with tie game handling.

## Learning Outcomes

Working through these programs helps developers understand:
- Input/output operations and user interaction
- Conditional logic and decision making
- Loop structures and iteration
- Functions and code organization
- Data structures (lists, tuples, dictionaries)
- GUI development with tkinter
- External library integration
- Error handling and validation
- Game logic implementation

## Future Enhancements

These programs can be extended with:
- Difficulty levels and settings
- Score persistence using file storage
- Enhanced graphics and animations
- Additional game modes
- Database integration for data storage
- Web-based versions
- Multiplayer support

## License

These educational projects are provided as learning resources.
