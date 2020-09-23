# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Averaging Measurements
# Date:        9/23/2020

# Defining variables
stored_amt = 0
user_amt = 0
running_avg = 0
running_min = 0
running_max = 0
counter = 0

# Asking for user input, the main loop
while user_amt >= 0:
    user_amt = int(input("Enter in data! "))
    if user_amt >= 0:
        if counter == 0:
            running_min = user_amt
        counter += 1
        stored_amt += user_amt
        if user_amt > running_max:
            running_max = user_amt
        if user_amt < running_min:
            running_min = user_amt
        running_avg = (running_avg + user_amt) / counter

# Print final values
print("Running max:",running_max)
print("Running min:",running_min)
print("Running avg:",running_avg)