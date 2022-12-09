#!/usr/bin/python3
# Day 9 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Functions
#-----------------------------------------------------
def chase(T, H):
    x_diff = H[0] - T[0]
    y_diff = H[1] - T[1]
    if (abs(x_diff) < 2 and abs(y_diff) < 2) or ( abs(y_diff) < 2 and abs(x_diff) < 2): return T        # No movement needed

    # Ensure knot doesnt move more than one space
    if x_diff < 0: x_diff = -1
    elif x_diff > 0: x_diff = 1
    if y_diff < 0: y_diff = -1
    elif y_diff > 0: y_diff = 1

    # Lateral move
    if x_diff == 0: return [T[0], T[1] + y_diff]
    elif y_diff == 0: return [T[0] + x_diff, T[1]]

    else: return [T[0] + x_diff, T[1] + y_diff]         # Diagonal move

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------

# (X_coordinate, Y_Coordinate)
H = [0,0]
T = [0,0]
unique_stops = ['0,0']

for line in lines:
    direction = line.split(' ')[0]
    distance = int(line.split(' ')[1])
    for i in range(distance):                               # Head Movement
        if direction == 'U':
            H[1] += 1
        elif direction == 'D':
            H[1] -= 1
        elif direction == 'L':
            H[0] -= 1
        elif direction == 'R':
            H[0] += 1

        T = chase(T, H)                                    # Tail Movement
        if f'{T[0]},{T[1]}' not in unique_stops: 
            unique_stops.append(f'{T[0]},{T[1]}')

print("Answer 1: ",len(unique_stops))
#print(unique_stops)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
H = [0,0]
knots = [[0,0]] * 9
unique_stops = ['0,0']

for line in lines:
    direction = line.split(' ')[0]
    distance = int(line.split(' ')[1])

    for i in range(distance):                               # Head Movement
        if direction == 'U':
            H[1] += 1
        elif direction == 'D':
            H[1] -= 1
        elif direction == 'L':
            H[0] -= 1
        elif direction == 'R':
            H[0] += 1
        
        knots[0] = chase(knots[0], H)                      # Tails Movement
        for i in range(1, len(knots)):
            knots[i] = chase(knots[i], knots[i-1])
        
        if f'{knots[8][0]},{knots[8][1]}' not in unique_stops: 
            unique_stops.append(f'{knots[8][0]},{knots[8][1]}')

print("Answer 2: ",len(unique_stops))