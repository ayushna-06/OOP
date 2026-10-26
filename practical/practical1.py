# Academic Integrity Statement
# filename: practical1.py
# author: AYUSHNA CHAPAGAIN
# student ID: 526482
# email: 526482@learning.eynesbury.edu.au
# date: 26/10/2026
# description: calculation of distance and kinetic energy
# This is my own work as defined by the Academic Integrity Policy

#task1
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

total_letters = 0
for day in days:
    total_letters = total_letters + len(day)

number_of_words = len(days)
average_length = total_letters / number_of_words

print("Average word length:", average_length)

#task2
def distance(speed, time):
    calculation = float(speed * time)
    return calculation

result_distance = distance(60, 100)
print("Distance:", result_distance)

#task 3
def kinetic_energy(mass, velocity):
    calculation_2 =  (1/2) * mass * (velocity ** 2)
    return calculation_2

result_ke = kinetic_energy(10, 60)
print("Kinetic Energy:", result_ke)

#task 4
class MovingObject:
    def __init__(self, velocity, mass):
        self.velocity = velocity
        self.mass = mass

    def distance(self, duration):
        return self.velocity * duration

    def kinetic_energy(self):
        return 0.5 * self.mass * (self.velocity ** 2)

#task 5
myMovingObject = MovingObject(6, 20)

print("Distance:", myMovingObject.distance(60))
print("Kinetic Energy:", myMovingObject.kinetic_energy())

