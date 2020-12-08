def count_trees(x_add, y_add, width, height):
    x, y = 0, 0
    trees = 0
    while y < height:
        if map_of_trees[y][x % width] == '#':
            trees = trees + 1
        x = x + x_add
        y = y + y_add
    return trees


map_of_trees = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        map_of_trees.append([char for char in line][:-1])
        line = f.readline()
width = len(map_of_trees[0])
height = len(map_of_trees)
trees_mul =     count_trees(1, 1, width, height)\
              * count_trees(3, 1, width, height)\
              * count_trees(5, 1, width, height)\
              * count_trees(7, 1, width, height)\
              * count_trees(1, 2, width, height)
print(trees_mul)
