busses = set()
arrival_time = -1
with open('input.txt', 'r') as f:
    line = f.readline()
    arrival_time = int(line[:-1])
    line = f.readline()
    busses.update(line[:-1].split(','))
busses.remove('x')
arrival_times = []
for bus in busses:
    arrival_times.append((int(bus) - (arrival_time % int(bus)), int(bus)))
    #  arrival_times[i] = (waiting_time, bus_number)
shortest_wait = sorted(arrival_times)[0]
print(shortest_wait[0] * shortest_wait[1])
