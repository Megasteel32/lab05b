# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Divisors
# Date:        9/24/2020

for i in range(2,101):
    for j in range(2,101):
        if i<= j and j%i == 0:
            print(i,"divides",j)