instructions = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        instructions.append(line[:-1])  # strip \n
        line = f.readline()

directions = ['N', 'E', 'S', 'W']
current_direction = 1  # start facing east
position = [0, 0]  # X (east to west), Y (north to south)


def move(direction, amount):
    if direction == 'N':
        position[1] += int(amount)
    elif direction == 'E':
        position[0] -= int(amount)
    elif direction == 'S':
        position[1] -= int(amount)
    elif direction == 'W':
        position[0] += int(amount)
    else:
        pass


for instruction in instructions:
    if instruction[0] in directions:
        move(instruction[0], instruction[1:])
    elif instruction[0] == 'L':
        current_direction = (current_direction - int(int(instruction[1:])/90)) % len(directions)
    elif instruction[0] == 'R':
        current_direction = (current_direction + int(int(instruction[1:])/90)) % len(directions)
    elif instruction[0] == 'F':
        move(directions[current_direction], instruction[1:])
print(abs(position[0]) + abs(position[1]))
