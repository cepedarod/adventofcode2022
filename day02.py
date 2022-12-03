#!/usr/bin/python3
# Day 2 Puzzle

#Read Input
input_file = "input.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
'''
A/X = Rock = 1
B/Y = Paper = 2
C/Z = Scissors = 3

loss = 0 
tie = 3 
win = 6 
'''
total_score = 0
for line in lines:
    if line.startswith('A'):
        if line.endswith('X'): total_score += 4
        elif line.endswith('Y'): total_score += 8
        elif line.endswith('Z'): total_score += 3
    elif line.startswith('B'):
        if line.endswith('X'): total_score += 1
        elif line.endswith('Y'): total_score += 5
        elif line.endswith('Z'): total_score += 9
    else:
        if line.endswith('X'): total_score += 7
        elif line.endswith('Y'): total_score += 2
        elif line.endswith('Z'): total_score += 6

print("Part 1 answer: ", total_score)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
'''
A = Rock = 1
B = Paper = 2
C = Scissors = 3

X = loss = 0 
Y = tie = 3 
Z = win = 6 
'''
total_score = 0
for line in lines:
    if line.startswith('A'):
        if line.endswith('X'): total_score += 3
        elif line.endswith('Y'): total_score += 4
        elif line.endswith('Z'): total_score += 8
    elif line.startswith('B'):
        if line.endswith('X'): total_score += 1
        elif line.endswith('Y'): total_score += 5
        elif line.endswith('Z'): total_score += 9
    else:
        if line.endswith('X'): total_score += 2
        elif line.endswith('Y'): total_score += 6
        elif line.endswith('Z'): total_score += 7
    
print("Part 2 answer: ", total_score)