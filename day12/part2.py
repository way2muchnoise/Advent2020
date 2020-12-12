import math

instructions = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        instructions.append(line[:-1])  # strip \n
        line = f.readline()

directions = ['N', 'E', 'S', 'W']
ship_position = [0, 0]  # X (east to west), Y (north to south)
waypoint_position_relative = [-10, 1]  # X (east to west), Y (north to south)


def move(direction, amount, position):
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
    return position


def rotate(angle, waypoint_position_relative):
    angle_r = math.radians(angle)
    waypoint_position_relative_rotated = [0, 0]
    waypoint_position_relative_rotated[0] = int(math.cos(angle_r)) * waypoint_position_relative[0] \
                                    - int(math.sin(angle_r)) * waypoint_position_relative[1]
    waypoint_position_relative_rotated[1] = int(math.sin(angle_r)) * waypoint_position_relative[0] \
                                    + int(math.cos(angle_r)) * waypoint_position_relative[1]
    return waypoint_position_relative_rotated


for instruction in instructions:
    if instruction[0] in directions:
        waypoint_position_relative = move(instruction[0], instruction[1:], waypoint_position_relative)
    elif instruction[0] == 'L':  # counter-clockwise => -angle
        waypoint_position_relative = rotate(-int(instruction[1:]), waypoint_position_relative)
    elif instruction[0] == 'R':  # counter-clockwise => +angle
        waypoint_position_relative = rotate(+int(instruction[1:]), waypoint_position_relative)
    elif instruction[0] == 'F':
        ship_position[0] = ship_position[0] + (int(instruction[1:]) * waypoint_position_relative[0])
        ship_position[1] = ship_position[1] + (int(instruction[1:]) * waypoint_position_relative[1])
print(abs(ship_position[0]) + abs(ship_position[1]))
