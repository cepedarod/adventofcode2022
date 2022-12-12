#!/usr/bin/python3
# Day 11 Puzzle

#-----------------------------------------------------
# Libraries
#-----------------------------------------------------
import string

#-----------------------------------------------------
# Functions & Classes
#-----------------------------------------------------
class node:
    def __init__(self, letter):
        self.left = ''
        self.up = ''
        self.right = ''
        self.down = ''
        self.coordinates = ''

        if letter.islower(): self.hight = string.ascii_lowercase.index(letter)
        elif letter == 'E': self.hight = 26
        elif letter == 'S': self.hight = 0
        else: self.hight = -1

# used to navigate nodes in specific directions
def make_key(x, y, direction):
    if direction == 'up': return f'{x}-{y-1}'
    elif direction == 'down': return f'{x}-{y+1}'
    elif direction == 'left': return f'{x-1}-{y}'
    elif direction == 'right': return f'{x+1}-{y}'

def print_path(path):
    print("PATH LENGTH: ", len(path))
    for node in path:
        print(node.coordinates)

    print("------------")
        

def find_path(node, hight, origin, path_taken, debug_ref):
    dead_end = True
    best_path = [0] * 10000
    new_path = []
    not_viable = False
    if node.coordinates == '1-2': 
            i = 0
    if (node.hight == -1 or 
        node.hight < hight or
        hight - node.hight < -1 or
        node in path_taken): 
            return dead_end, path_taken      # Dead End

    elif node.hight == 26:                                                      # Found Target
        #path_taken.append(node)
        #if debug_ref in path_taken: print_path(path_taken)
        return False, path_taken

    #elif node in path_taken: return dead_end, path_taken                        # Repeat node in path

    elif origin == 'left':
        new_path = path_taken
        path_taken.append(node)
        not_viable, new_path = find_path(node.up, node.hight, 'down', path_taken, debug_ref)
        if node.coordinates == '1-1': 
            i=0
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.right, node.hight, 'left', path_taken, debug_ref)
        if node.coordinates == '1-1': 
            i=0
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.down, node.hight, 'up', path_taken, debug_ref)
        if node.coordinates == '1-1': 
            print_path(new_path)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

    elif origin == 'right':
        path_taken.append(node)
        not_viable, new_path = find_path(node.up, node.hight, 'down', path_taken, debug_ref)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.left, node.hight, 'right', path_taken, debug_ref)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.down, node.hight, 'up', path_taken, debug_ref)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

    elif origin == 'up':
        path_taken.append(node)
        not_viable, new_path = find_path(node.left, node.hight, 'right', path_taken, debug_ref)
        if node.coordinates == '1-2': 
            i = 0
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.right, node.hight, 'left', path_taken, debug_ref)
        if node.coordinates == '1-1': 
            print_path(new_path)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.down, node.hight, 'up', path_taken, debug_ref)
        if node.coordinates == '1-2': 
            i = 0
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path
        

    elif origin == 'down':
        path_taken.append(node)
        not_viable, new_path = find_path(node.up, node.hight, 'down', path_taken, debug_ref)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.right, node.hight, 'left', path_taken, debug_ref)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path

        not_viable, new_path = find_path(node.left, node.hight, 'right', path_taken, debug_ref)
        if not_viable == False and len(new_path) < len(best_path):  best_path = new_path
    i = 0
    return False, best_path
#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
#input_file = "input.txt"
input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)


#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
# Initialize nodes
x_max = len(lines[0]) - 1
y_max = len(lines) - 1

# Create all node nodes and add them to map; No adjancancies
all_nodes = {}
for y, line in enumerate(lines):
    for x, n in enumerate(line):
        key = f'{x}-{y}'
        all_nodes[key] = node(n)
        all_nodes[key].coordinates = key
        if n == 'S': start_point = all_nodes[key]

# Now that all nodes are in map, link adjecent nodes
for key in all_nodes:
    x = int(key.split('-')[0])
    y = int(key.split('-')[1])

    # x axis adjacencies
    if int(x) == 0: 
        all_nodes[key].left = node('X')
        all_nodes[key].right = all_nodes[make_key(x,y,"right")]
    elif int(x) == x_max: 
        all_nodes[key].right = node('X')
        all_nodes[key].left = all_nodes[make_key(x,y,"left")]
    else:
        all_nodes[key].left = all_nodes[make_key(x,y,"left")]
        all_nodes[key].right = all_nodes[make_key(x,y,"right")]
    i = 0
    # y axis adjacencies
    if int(y) == 0: 
        all_nodes[key].up = node('X')
        all_nodes[key].down = all_nodes[make_key(x,y,"down")]
    elif int(y) == y_max: 
        all_nodes[key].down = node('X')
        all_nodes[key].up = all_nodes[make_key(x,y,"up")]
    else:
        all_nodes[key].up = all_nodes[make_key(x,y,"up")]
        all_nodes[key].down = all_nodes[make_key(x,y,"down")]
    i = 0
# Solve
best_path_length = 10000
dead_end, new_path = find_path(start_point.left, start_point.hight, 'right', [start_point], all_nodes['1-2'])
if not dead_end and len(new_path) < best_path_length: best_path_length = len(new_path)

dead_end, new_path = find_path(start_point.up, start_point.hight, 'down', [start_point], all_nodes['1-2'])
if not dead_end and len(new_path) < best_path_length: best_path_length = len(new_path)

dead_end, new_path = find_path(start_point.right, start_point.hight, 'left', [start_point], all_nodes['1-2'])
if not dead_end and len(new_path) < best_path_length: best_path_length = len(new_path)

dead_end, new_path = find_path(start_point.down, start_point.hight, 'up', [start_point], all_nodes['1-2'])
b = new_path
if not dead_end and len(new_path) < best_path_length: best_path_length = len(new_path)

for item in b:
    for key in all_nodes:
        if all_nodes[key] == item: 
            print(key)
            break
print(best_path_length)