#!/usr/bin/python3
# Day 4 Puzzle

#Read Input
input_file = "input.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
# Check for ranges that complitly encompass the other
part_1_answer = 0
for line in lines:
    a,b = line.split(',')            # Split line into both ranges
    if (int(a.split('-')[0]) <= int(b.split('-')[0]) and (int(a.split('-')[1]) >= int(b.split('-')[1]))) or (int(a.split('-')[0]) >= int(b.split('-')[0]) and (int(a.split('-')[1]) <= int(b.split('-')[1]))):
        part_1_answer += 1
    
print("Part 1 Answer: ", part_1_answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
# Check for ranges that have any kind of overlap
part_2_answer = 0
for line in lines:
    a,b = line.split(',')
    if (int(a.split('-')[1]) >= int(b.split('-')[0]) and int(a.split('-')[0]) <= int(b.split('-')[1])) or (int(a.split('-')[0]) <= int(b.split('-')[1]) and int(a.split('-')[1]) >= int(b.split('-')[0])):
        part_2_answer += 1

print("Part 2 Answer: ", part_2_answer)
