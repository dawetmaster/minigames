# This is an improved water jug with randomized number of desired amount of water
# and randomized jugs' capacity and sure that's not too easy
# Author: Andika N. Hilmy
# Date: 29 - Oct - 2020
# Language: Python 3.8

# Libraries
from os import system, name
import random
import math
import sys
import time

# Classes
class jug:
    def __init__(self, valuepart, capacity):
        self.value = valuepart
        self.fill = ['     '] * capacity
    def update_fill(self, height):
        for i in range(len(self.fill)): # fills from 0 to top since liquid fills from the bottom
            if i < height:
                self.fill[i] = chr(0x2593)*5 # dark shade char
            else:
                self.fill[i] = '     '

# Functions and Procedures

# define bordered text function
# this is important as general function
# to make this framed to gain user focus
def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines) + 2
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (' ' + s + ' ' * (width))[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# define procedure to show jugs graphically
def show_jugs(val1, val2):
    print("\n")
    print("".center(25), "┐     ┌".center(25))
    for i in range(capacity_2-1, capacity_1, -1):
        print("".center(25), f"│{jug2.fill[i]}│".center(25))
    print("┐     ┌".center(25), f"│{jug2.fill[capacity_1]}│".center(25))
    for i in range(capacity_1-1, -1, -1):
        print(f"│{jug1.fill[i]}│".center(25), f"│{jug2.fill[i]}│".center(25))
    print("└─────┘".center(25), "└─────┘".center(25))
    print("\n")
    print(f"{jug1.value} gallon(s)".center(25),f"{jug2.value} gallon(s)".center(25))
    print(f"{capacity_1}-gallon jug".center(25),f"{capacity_2}-gallon jug".center(25))

# Syntax

# clear screen when entering the game
clear()

# randomize jugs and water amount until it gets some right combination that's not too easy
while True:
    capacity_1 = random.randint(1, 12)
    capacity_2 = random.randint(1, 12)
    desired_amt = random.randint(1, max(capacity_1, capacity_2))

    # check randomized numbers, if it's not too easy it will continue, otherwise it will repeat
    if (desired_amt % math.gcd(capacity_1, capacity_2) == 0) and desired_amt != capacity_1 and desired_amt != capacity_2 and desired_amt != capacity_2 - capacity_1 and capacity_1 < capacity_2:
        break

# set jugs' capacity
jug1 = jug(0, capacity_1)
jug2 = jug(0, capacity_2)

# print an intro screen
print(f"""A Water Jug Problem: You are given two jugs, a {capacity_1}-gallon one and a {capacity_2}-gallon
one, a pump which has unlimited water which you can use to fill the jug, and
the ground on which water may be poured. Neither jug has any measuring
markings on it. How can you get exactly {desired_amt} gallons of water in any jug provided?

PRESS ENTER TO CONTINUE""")
_ = input() # user will press enter then clears screen
clear()

# game starts
steps = 0
while jug1.value != desired_amt and jug2.value != desired_amt:

    # show jugs graphically
    show_jugs(jug1.value, jug2.value)

    # show options
    print(bordered(f"""You must fill either jugs with {desired_amt} gallons of water.
You are given 6 options to solve this problem.

(1) Fill the {capacity_1}-gallon jug
(2) Fill the {capacity_2}-gallon jug
(3) Empty the {capacity_1}-gallon jug
(4) Empty the {capacity_2}-gallon jug
(5) Move {capacity_1}-gallon jug contents to {capacity_2}-gallon jug
(6) Move {capacity_2}-gallon jug contents to {capacity_1}-gallon jug
(x) Leave as it is and do otherwise (Exit the game)

Now, it's your turn."""))
    
    # print number of steps then add
    print(f"Steps done: {steps}")
    steps += 1

    # get user input
    selected = input("Enter your option: ")
    
    # Case "selected" analysis
    if selected == "1": # Fill the {capacity_1}-gallon jug
        jug1.value = capacity_1
    elif selected == "2": # Fill the {capacity_2}-gallon jug
        jug2.value = capacity_2
    elif selected == "3": # Empty the {capacity_1}-gallon jug
        jug1.value = 0
    elif selected == "4": # Empty the {capacity_2}-gallon jug
        jug2.value = 0
    elif selected == "5": # Move {capacity_1}-gallon jug contents to {capacity_2}-gallon jug
        if jug1.value > 0:
            jug2.value = jug1.value + jug2.value
            if jug2.value > capacity_2:
                jug1.value = jug2.value - capacity_2
                jug2.value = jug2.value - jug1.value
            else:
                jug1.value = 0
        else:
            steps = steps - 1
    elif selected == "6": # Move {capacity_2}-gallon jug contents to {capacity_1}-gallon jug
        if jug2.value > 0:
            jug1.value = jug1.value + jug2.value
            if jug1.value > capacity_1:
                jug2.value = jug1.value - capacity_1
                jug1.value = jug1.value - jug2.value
            else:
                jug2.value = 0
        else:
            steps = steps - 1
    elif selected == "x" or selected == "X": # Leave as it is
        while True:
            ans = input("Are you sure to exit the game (y/n)? ")
            if ans == "y":
                sys.exit()
            elif ans == "n":
                steps -= 1
                break
    else: # wrong option
        steps -= 1
        print("Wrong option. Please try again.")
        time.sleep(2)

    # go to next scene by clear screen and update jug graphics
    jug1.update_fill(jug1.value)
    jug2.update_fill(jug2.value)
    clear()

# game ended and here's the results
print("Here's your result.")
show_jugs(jug1.value, jug2.value) # show jug graphics
print("\n")
print(f"You solved it in {steps} steps.")
print("\n")
print("GAME OVER.")
clear()