# coding=utf-8
"""
21. Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with
a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a
sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
import math


def get_distance(idx, idy):
    return math.sqrt(idx**2 + idy**2)


pos = {"x": 0, "y": 0}

moves = {"UP": [0, 1], "DOWN": [0, -1], "LEFT": [-1, 0], "RIGHT": [1, 0]}

while True:
    line = raw_input()

    if len(line.split()) != 2:
        break

    direction, steps = line.split()

    if direction in moves:
        pos["x"] += moves[direction][0] * int(steps)
        pos["y"] += moves[direction][1] * int(steps)

distance = get_distance(pos["x"], pos["y"])

print int(round(distance))
