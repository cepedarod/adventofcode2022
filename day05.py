#!/usr/bin/python3
# Day 5 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------

input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

all_stacks = [[] for i in range(9)]                                                      # Initialize list of list that will represent the stacks of creates

# convert raw lines in to the correct stacks specified in the puzzle
for line in range(8):                                                                    # 8 Total Stacks
    for stack, box in enumerate(range(1,len(lines[line]),4)):                            # Iterate only through the carracters of interest
        if lines[line][box] != ' ': all_stacks[stack].insert(0,lines[line][box])         # If character is not blank space, push to correct stack

instructions = lines[10:]                                                                # Get only create movement instruction set
#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
# Creates Move 1 at a time
'''
# Make Crate Movements
for i in instructions:
    i = i.replace("move ", '')                                                           # Remove words from input line
    i = i.replace(" from", '')                                                           # leave numbers only separated by a space
    i = i.replace(" to", '')
    parameters = [int(p) for p in i.split(" ")]                                          # Convert Parameters to ints
    quantity = parameters[0]
    source = parameters[1] - 1                                                           # subtract 1 since list containing stacks is 0-indexed 
    target = parameters[2] - 1

    #print(quantity, source, target)

    for rep in range(quantity):                                                          # Move removed item from source stack to top of target stack
        all_stacks[target].append(all_stacks[source].pop())
    
print([stack[-1] for stack in all_stacks])                                               # PART 1 ANSWER
'''
#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
# Creates Move multiple at a time

for i in instructions:
    i = i.replace("move ", '')                                                           # Remove words from input line
    i = i.replace(" from", '')                                                           # leave numbers only separated by a space
    i = i.replace(" to", '')
    parameters = [int(p) for p in i.split(" ")]                                          # Convert Parameters to ints
    quantity = parameters[0] * -1                                                        # Convert to negative since top Box on list is last element
    source = parameters[1] - 1
    target = parameters[2] - 1                                                           # subtract 1 since list containing stacks is 0-indexed

    all_stacks[target] += all_stacks[source][quantity:]                                  # Add to target stack last n elemenets of the source stack (e.g. [-3:] for n = 3)
    all_stacks[source] = all_stacks[source][:quantity]                                   # Remove last n elements from source stack
    
print([stack[-1] for stack in all_stacks])                                               # PART 2 ANSWER