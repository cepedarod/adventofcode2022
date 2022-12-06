#!/usr/bin/python3
# Day 6 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------

input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

input = lines[0]

#-----------------------------------------------------
# Solution
#-----------------------------------------------------
def solve(target_length):
    code = []
    for answer, letter in enumerate(input):
        if len(code) == target_length:
            print("Answer : ", answer)
            break
        while letter in code: code = code[1:]
        code.append(letter) 

solve(4)
solve(14)
