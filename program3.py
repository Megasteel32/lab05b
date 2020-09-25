# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Angery Bird
# Date:        9/25/2020

from math import cos, sin, radians, tan
import matplotlib.pyplot as plt

# Defining variables
angle = 0
velocity = 0
vx = 0
vy = 0
var_range = 0
target = 202.4
gravity = 9.8
workyworky = 0
xlist = []
ylist = []
nexty = 0

# Requesting user input for variables
velocity = int(input("What is the velocity for Red? "))

for angle in range(1, 91):
    vx = velocity * cos(radians(angle))
    vy = velocity * sin(radians(angle))
    var_range = (2 * vx * vy) / gravity
    if var_range >= 202.4:
        workyworky = 1
        break
final_range = var_range
final_angle = angle
if workyworky == 0:
    print("No Solutions Found!")

if workyworky == 1:
    for x in range(1000):
        nexty = (velocity * x) * sin(angle) - ((0.5 * gravity) * (x ** 2)) * 0.1
        if nexty >= 0:
            ylist.append(nexty)
            xlist.append(x * 0.1)
        else:
            ylist.append(nexty)
            xlist.append(x * 0.1)
            break

if workyworky == 1:
    print("The final angle was {} and the final range was {}".format(final_angle, round(final_range,2)))
    plt.plot(xlist, ylist)
    plt.xlabel("x axis, 1s")
    plt.ylabel("y axis, 0.1m")
    plt.show()

# Mars is really not happening. Sorry Elon Musk.