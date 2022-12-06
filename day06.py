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
# Part 1
#-----------------------------------------------------
code = []
for answer, letter in enumerate(input):
    if len(code) == 4:
        print("Answer 1: ", answer)
        break
    while letter in code: code = code[1:]
    code.append(letter)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
code = []
for answer, letter in enumerate(input):
    if len(code) == 14:
        print("Answer 2: ", answer)
        break
    while letter in code: code = code[1:]
    code.append(letter)
