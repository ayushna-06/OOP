# Academic Integrity Statement
# filename: app.py
# author: AYUSHNA CHAPAGAIN
# student ID: 526482
# email: 526482@learning.eynesbury.edu.au
# date: 22/10/2026
# description: app class
# This is my own work as defined by the Academic Integrity Policy

from coin import Coin
from dice import Dice

class App:
    def __init__(self):
        self.home()
        return

    def home(self):
        print("HOME")
        options = [
            ("Toss Coin", self.toss),
            ("Roll Dice", self.roll),
            ("Close App", self.close)
        ]
        for option in options:
            index = options.index(option)
            print(index+1, option[0])

        user_selection = input("Please select an option: ")
        try:
            user_index = int(user_selection)-1
            option = options[user_index]
            print(option[0])
            option[1]()
        except Exception as e:
            print(e)
            self.home()

        return

    def toss(self):
        coin = Coin()
        value = coin.toss()
        if value == 0:
            print("Heads")
        elif value == 1:
            print("Tails")
        self.home()
        return

    def roll(self):
        dice = Dice(6)
        value = dice.roll()
        print("Value:", value)
        self.home()
        return

    def close(self):
        print("Closing App")
        return

App()