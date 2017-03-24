import random
import math
from math import pi
radius = random.randint(1,20)
found = False
counter = 0
while not found:
    counter += 1
    guess = int(input("Circle area is %.2f. What is the radius [1-20]?\n" % (pi*radius**2)))
    if guess == radius:
        print("Well done! You are correct.")
        found = True
        print("Number of attempts:", counter)
        print("Program Terminated")
    elif radius > guess:
        print("Wrong, Guess again.\nYour value is too small")
    elif radius < guess:
        print("Wrong, Guess again.\nYour value is too large")