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
        self.dead_end = False
        self.letter = letter
        self.explored = False
        self.best_route = False
        self.final_path = False

        if letter == 'E': self.dist_to_end = 0
        else: self.dist_to_end = -1

        if letter.islower(): self.hight = string.ascii_lowercase.index(letter)
        elif letter == 'E': self.hight = 26
        elif letter == 'S': self.hight = 0
        else: self.hight = -1

    def make_adjacency_list(self):
        self.adjacencies = [self.up, self.down, self.left, self.right]

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


def find_path(node, hight, origin, path_taken, best_path):
    node.explored = True
    is_viable = False

    if (node.hight == -1 or 
        node in path_taken or
        len(path_taken) + 1 >= len(best_path) or 
        node.dead_end
        ): 
            return best_path                 # Dead End

    elif node.hight == 26:
        if best_path == [] or len(path_taken) < len(best_path):
            return path_taken
        else: return best_path     # Found Target

    else:
        ref_path = path_taken.copy()
        ref_path.append(node)

        if origin != 'down' and node.down.hight - node.hight <= 1:
            new_path = find_path(node.down, node.hight, 'up', ref_path, best_path)
            if new_path != best_path: 
                is_viable = True
                if len(new_path) < len(best_path): best_path = new_path

        if origin != 'up' and node.up.hight - node.hight <= 1:
            new_path = find_path(node.up, node.hight, 'down', ref_path, best_path)
            if new_path != best_path: 
                is_viable = True
                if len(new_path) < len(best_path): best_path = new_path
                
        if origin != 'left' and node.left.hight - node.hight <= 1:
            new_path = find_path(node.left, node.hight, 'right', ref_path, best_path)
            if new_path != best_path: 
                is_viable = True
                if len(new_path) < len(best_path): best_path = new_path
        
        if origin != 'right' and node.right.hight - node.hight <= 1:
            new_path = find_path(node.right, node.hight, 'left', ref_path, best_path)
            if new_path != best_path: 
                is_viable = True
                if len(new_path) < len(best_path): best_path = new_path

    if not is_viable:
        node.dead_end = True
        return best_path

    else: return best_path



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
        elif n == 'E': end_point = all_nodes[key]

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
    
    all_nodes[key].make_adjacency_list()

# Solve
best_path = [0] * 500
best_path = find_path(start_point, 0, 'start', [], best_path)

best_path_length = len(best_path)
print_path(best_path)

for node in best_path:
    node.final_path = True

print(best_path_length)
row = ''
row_num = ''
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if all_nodes[f'{x}-{y}'].final_path == True: row_num += '$'
        else: row_num += '.'

        if all_nodes[f'{x}-{y}'] == start_point: row += 'S'
        elif all_nodes[f'{x}-{y}'].hight == 26: row += 'E'
        elif all_nodes[f'{x}-{y}'].dead_end: row += '#'
        else: row += '.'
    print(row, "     ", row_num)
    row = ''
    row_num = ''
