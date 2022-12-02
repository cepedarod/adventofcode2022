#!/usr/bin/python3
# Day 1 Puzzle

#Read Input
input_file = "input.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
largest_sum = 0
current_sum = 0
for item in lines:
    if item: current_sum += int(item)
    else:
        if current_sum > largest_sum: largest_sum = current_sum
        current_sum = 0

print("Part 1 answer: ", largest_sum)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
sums = []
current_sum = 0
for item in lines:
    if item: current_sum += int(item)
    else: 
        sums.append(current_sum)
        current_sum = 0
sums.sort(reverse=True)
print("3 Largest Sums: ", sums[:3])
print("Part 2 answer: ", sum(sums[:3]))