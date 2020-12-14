from math import gcd

busses = []
with open('input.txt', 'r') as f:
    line = f.readline()
    line = f.readline()
    busses = line[:-1].split(',')
busses_order = []
for i in range(len(busses)):
    if busses[i] == 'x':
        pass
    else:
        busses_order.append((i, int(busses[i])))  # busses_order[i] = (index, bus_number)


# Least Common Multiple
def lcm(x, y):
    return (x * y) // gcd(x, y)


def find_sequential_start(busses_order):
    if len(busses_order) == 1:
        return busses_order[0][1] - busses_order[0][0], busses_order[0][1]  # bus number - offset, repeat cycle
    sequential_start_time, repeat_cycle = find_sequential_start(busses_order[:-1])
    print(sequential_start_time)
    last_bus = busses_order[-1]
    # has to be greater than the next bus number (first arrival) and remainder after division needs to match offset
    while not (sequential_start_time > last_bus[1] and (sequential_start_time+last_bus[0]) % last_bus[1] == 0):
        sequential_start_time += repeat_cycle
    return sequential_start_time, lcm(repeat_cycle, last_bus[1])  # start of sequence


print(find_sequential_start(busses_order)[0])
