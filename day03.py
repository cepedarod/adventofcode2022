#!/usr/bin/python3
# Day 3 Puzzle

#-----------------------------------------------------
# Libraries
#-----------------------------------------------------
import string


#Read Input
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------

all_common_characters = []
for line in lines:
    a, b = set(line[:len(line)//2]), set(line[len(line)//2:])         # Split string into 2 halves and convert to sets (a and b)
    all_common_characters += list(a&b)                                # Use the & opperator to find all common elements in 2 sets, then add to master list

part_1_answer = 0
for letter in all_common_characters:                                                            # string.ascii_lowercase indexes lowercase alphabet from 0(a) to 25(z)
    if letter.isupper(): part_1_answer += string.ascii_lowercase.index(letter.lower()) + 27     # If character is uppercase, add 27 to the index to match puzzle index values
    else: part_1_answer += string.ascii_lowercase.index(letter.lower()) + 1                     # If character is lowercase, add 1 to the index to match puzzle index values
    
#Part 1 Answer
print("Part 1 Answer: ", part_1_answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
all_common_characters = []
for  x in range(0,len(lines), 3):                                                               # Iterate through list of strings 3 at a time
    a, b, c = set(lines[x]), set(lines[x+1]), set(lines[x+2])                                   # Convert each string in the group of 3 into a set
    all_common_characters += list(a&b&c)                                                        # Compare sets using the & opperator to find common element

part_2_answer = 0
for letter in all_common_characters:                                                            # string.ascii_lowercase indexes lowercase alphabet from 0(a) to 25(z)
    if letter.isupper(): part_2_answer += string.ascii_lowercase.index(letter.lower()) + 27     # If character is uppercase, add 27 to the index to match puzzle index values
    else: part_2_answer += string.ascii_lowercase.index(letter.lower()) + 1                     # If character is lowercase, add 1 to the index to match puzzle index values

#Part 2 Answer
print("Part 2 Answer: ", part_2_answer)

