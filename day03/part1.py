map_of_trees = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        map_of_trees.append([char for char in line][:-1])
        line = f.readline()
width = len(map_of_trees[0])
x, y = 0, 0
x_add = 3
y_add = 1
trees = 0
while y != len(map_of_trees):
    if map_of_trees[y][x % width] == '#':
        trees = trees + 1
    x = x + x_add
    y = y + y_add
print(trees)
