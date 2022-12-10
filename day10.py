#!/usr/bin/python3
# Day 10 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
reg_x = 1
cycle = 1
signal_strength_total = 0
cycle_of_interest = 20
process_time = 0
for line in lines:
    if line == 'noop': process_time = 1
    elif line.startswith('addx'): process_time = 2

    for c in range(process_time):
        if cycle == cycle_of_interest:
            signal_strength_total += (cycle * reg_x)
            cycle_of_interest += 40
        
        cycle += 1
    
    if line.startswith('addx'): reg_x += int(line.split(' ')[1])

print('Part 1 Answer: ', signal_strength_total)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
reg_x = 1
cycle = 0
process_time = 0
display_line = ''
exec_done = 0
for line in lines:
    if line == 'noop': process_time = 1
    elif line.startswith('addx'): process_time = 2
    
    for c in range(process_time):
        if abs(reg_x - (cycle % 40)) <= 1: display_line += '#'
        else: display_line += '.'

        cycle += 1
        if cycle == 40:
            print(display_line)
            display_line = ''
            cycle = 0
        
    if line.startswith('addx'): reg_x += int(line.split(' ')[1])

