#!/usr/bin/python3
# Day 7 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)
lines = lines[1:]                                               # Skip first line since we know we start in root folder

#-----------------------------------------------------
# Functions & Classes
#-----------------------------------------------------
class node:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = size
        if size == 0: self.type = 'folder'
        else: self.type = 'file'

    def __eq__(self, other):                        # Allows for checking if object is in list by name
        return self.name == other.name

def find_dirs(dir, target_size, dir_list, min_max):     # min_max determins if we are looking for dirs smaller or bigger than target_size
    size_sum = 0
    for item in dir.children:
        if dir.children[item].type == 'file':
            size_sum += dir.children[item].size
        else:
            dir_size = find_dirs(dir.children[item], target_size, dir_list, min_max)
            size_sum += dir_size

    dir.size = size_sum
    if min_max == 'max' and size_sum <= target_size: dir_list.append(dir)
    elif min_max == 'min' and size_sum >= target_size: dir_list.append(dir)

    return size_sum

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
root = node('root', '', 0)

#Build Directory Tree
current_folder = root
for line in lines:
    if line == '$ cd ..': current_folder = current_folder.parent
    elif line == '$ cd /': current_folder = root
    elif line.startswith('$ cd'):
        f_name = line.split(' ')[2]
        current_folder = current_folder.children[f_name]
    elif line.startswith('dir'):
        f_name = line.split(' ')[1]
        if f_name not in current_folder.children: 
            current_folder.children[f_name] = node(f_name, current_folder, 0)
    elif line != '$ ls':
        f_name = line.split(' ')[1]
        file_size = int(line.split(' ')[0])
        if f_name not in current_folder.children: 
            current_folder.children[f_name] = node(f_name, current_folder, file_size)

# Solve for Part 1
dir_list = []
target_size = 100000
answer = 0
find_dirs(root, target_size, dir_list, 'max')

for dir in dir_list:
    if dir.size <= target_size: answer += dir.size

print('Answer Part 1: ', answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
needed_space = 30000000 - (70000000 - root.size)

# Solve for Part 2
dir_list = []
target_size = needed_space
find_dirs(root, target_size, dir_list, 'min')

answer = 70000000
for dir in dir_list:
    if dir.size < answer: answer = dir.size

print('Answer Part 2: ', answer)
