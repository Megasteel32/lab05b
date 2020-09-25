# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Angery Bird
# Date:        9/25/2020

from math import cos, sin, radians

# Defining variables
angle = 0
velocity = 0
vx = 0
vy = 0
var_range = 0
target = 202.4
gravity = 9.8
counter = 0


# Requesting user input for variables
velocity = int(input("What is the velocity for Red? "))

for angle in range(1,91):
    vx = velocity * cos(radians(angle))
    vy = velocity * sin(radians(angle))
    range = (2 * vx * vy) / gravity
    counter += 1
    print(round(range,2),counter)
