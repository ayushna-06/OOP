# Academic Integrity Statement
# filename: coin.py
# author: AYUSHNA CHAPAGAIN
# student ID: 526482
# email: 526482@learning.eynesbury.edu.au
# date: 22/10/2026
# description: Coin class
# This is my own work as defined by the Academic Integrity Policy

import random

class Coin:
    def __init__(self):
        self.set_value()

    def get_value(self):
        return self._value

    def set_value(self):
        self._value = random.randint(0, 1)

    def toss(self):
        self.set_value()
        return self.get_value()


if __name__ == "__main__":
    coin = Coin()
    print(coin.toss())
    print(coin.toss())
    print(coin.toss())