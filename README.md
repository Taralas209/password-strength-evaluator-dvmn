# Password Strength Evaluator

This program is an interactive text-based application, built with Python and the urwid library, that rates the strength of a password based on several criteria.

## Installation

Make sure you have Python (3.6 or higher is recommended) and pip (Python package installer) installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

You also need to install urwid. You can do it with pip:

```pip install urwid```

## Running the Program
After you have installed the necessary dependencies, you can run the program with Python:
```python main.py```

This will launch an interactive text-based interface where you can enter a password. The program will calculate and display the strength of your password, scoring it based on the following criteria:

It is more than 12 characters long.
It contains digits.
It contains letters.
It contains uppercase letters.
It contains lowercase letters.
It contains special symbols.
The password strength score will update in real-time as you type your password.

The mask option for the password field is enabled by default. Therefore, the actual characters of the password won't be displayed, providing a better security measure.

## Program Description
The program utilizes two main files. The first one contains functions that evaluate different characteristics of a password, such as its length, and whether it contains digits, letters (both lower and upper case), and symbols.

The second file contains the main function that establishes the interactive interface. It connects the urwid Edit and Text widgets, setting up a password field and an area to display the password strength score. As the password changes, it emits the 'change' signal, which is connected to the show_score function that calculates and updates the score.

##Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
