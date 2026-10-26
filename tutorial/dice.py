# Academic Integrity Statement
# filename: dice.py
# author: AYUSHNA CHAPAGAIN
# student ID: 526482
# email: 526482@learning.eynesbury.edu.au
# date: 22/10/2026
# description: dice class
# This is my own work as defined by the Academic Integrity Policy

import random

class Dice:
    def __init__(self, sides):
        self._sides = sides
        self.set_value()
        return

    def get_sides(self):
        return self._sides

    def set_value(self):
        self._value = random.randint(0, self.get_sides())
        return

    def get_value(self):
        return self._value

    def roll(self):
        self.set_value()
        return self.get_value()