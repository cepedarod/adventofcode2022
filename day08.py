#!/usr/bin/python3
# Day 8 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Functions & Classes
#-----------------------------------------------------
class tree:
    def __init__(self, size):
        self.size = size
        self.left = ''
        self.up = ''
        self.right = ''
        self.down = ''

def make_key(x, y, direction):                                      # used to navigate trees in specific directions
    if direction == 'up': return str(x) + '-' + str(y-1)
    elif direction == 'down': return str(x) + '-' + str(y+1)
    elif direction == 'left': return str(x-1) + '-' + str(y)
    elif direction == 'right': return str(x+1) + '-' + str(y)

def is_visible(tree_node, hight, direction):
    if direction == 'left':
        if tree_node.size == -1: return True
        elif tree_node.size >= hight: return False
        else: return is_visible(tree_node.left, hight, direction)
    elif direction == 'right':
        if tree_node.size == -1: return True
        elif tree_node.size >= hight: return False
        else: return is_visible(tree_node.right, hight, direction)
    if direction == 'up':
        if tree_node.size == -1: return True
        elif tree_node.size >= hight: return False
        else: return is_visible(tree_node.up, hight, direction)
    elif direction == 'down':
        if tree_node.size == -1: return True
        elif tree_node.size >= hight: return False
        else: return is_visible(tree_node.down, hight, direction)

def view_distance(tree_node, hight, view_range, direction):
    if direction == 'left':
        if tree_node.size == -1: return view_range
        elif tree_node.size >= hight: return view_range + 1
        else: return view_range + view_distance(tree_node.left, hight, view_range, direction) + 1
    elif direction == 'right':
        if tree_node.size == -1: return view_range
        elif tree_node.size >= hight: return view_range + 1
        else: return view_range + view_distance(tree_node.right, hight, view_range, direction) + 1
    if direction == 'up':
        if tree_node.size == -1: return view_range
        elif tree_node.size >= hight: return view_range + 1
        else: return view_range + view_distance(tree_node.up, hight, view_range, direction) + 1
    elif direction == 'down':
        if tree_node.size == -1: return view_range
        elif tree_node.size >= hight: return view_range + 1
        else: return view_range + view_distance(tree_node.down, hight, view_range, direction) + 1

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------

# Initialize tree nodes
x_max = len(lines[0]) - 1
y_max = len(lines) - 1

# Create all tree nodes and add them to map; No adjancancies
all_trees = {}
for y, row_of_trees in enumerate(lines):
    for x, t in enumerate(row_of_trees):
        key = str(x) + '-' + str(y)                                 # use tree coordinates in 'x-y' format as keys
        all_trees[key] = tree(int(t))

# Now that all trees are in map, link adjecent nodes
for key in all_trees:
    x = int(key.split('-')[0])
    y = int(key.split('-')[1])
    # x axis adjacencies
    if int(x) == 0: 
        all_trees[key].left = tree(-1)
        all_trees[key].right = all_trees[make_key(x,y,"right")]
    elif int(x) == x_max: 
        all_trees[key].right = tree(-1)
        all_trees[key].left = all_trees[make_key(x,y,"left")]
    else:
        all_trees[key].left = all_trees[make_key(x,y,"left")]
        all_trees[key].right = all_trees[make_key(x,y,"right")]
    # y axis adjacencies
    if int(y) == 0: 
        all_trees[key].up = tree(-1)
        all_trees[key].down = all_trees[make_key(x,y,"down")]
    elif int(y) == y_max: 
        all_trees[key].down = tree(-1)
        all_trees[key].up = all_trees[make_key(x,y,"up")]
    else:
        all_trees[key].up = all_trees[make_key(x,y,"up")]
        all_trees[key].down = all_trees[make_key(x,y,"down")]

# Calculate Part 1 Answer    
total_visible_trees = 0
for key in all_trees:
    if key.startswith('0-') or key.endswith('-0') or key.startswith(str(x_max)) or key.endswith(str(y_max)):        # If edge tree
        total_visible_trees += 1

    elif (
        is_visible(all_trees[key].left, all_trees[key].size, 'left') or
        is_visible(all_trees[key].right, all_trees[key].size, 'right') or
        is_visible(all_trees[key].up, all_trees[key].size, 'up') or
        is_visible(all_trees[key].down, all_trees[key].size, 'down')
    ): total_visible_trees+= 1

print("Answer 1: ", total_visible_trees)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
best_tree = 0
for key in all_trees:
    # If not edge
    if (not key.startswith('0-') and 
        not key.endswith('-0') and  
        not key.startswith(str(x_max)) and  
        not key.endswith(str(y_max))
    ):
        range_l = view_distance(all_trees[key].left, all_trees[key].size, 0, 'left')
        range_r = view_distance(all_trees[key].right, all_trees[key].size, 0, 'right')
        range_u = view_distance(all_trees[key].up, all_trees[key].size, 0, 'up')
        range_d = view_distance(all_trees[key].down, all_trees[key].size, 0, 'down')

        scenic_score = range_l*range_r*range_u*range_d
        if scenic_score > best_tree: best_tree = scenic_score
    
print("Answer 2: ", best_tree)
