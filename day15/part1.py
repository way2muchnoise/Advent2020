starting_numbers = []
with open('input.txt', 'r') as f:
    line = f.readline()
    starting_numbers.extend(map(int, line[:-1].split(',')))

said_numbers = []
current_turn = 0
said_numbers.extend(starting_numbers)
current_turn += len(starting_numbers)
while current_turn < 2020:
    if said_numbers[-1] not in said_numbers[:-1]:  # never been spoken before
        said_numbers.append(0)
    else:  # been spoken before
        prev_spoken_index = len(said_numbers[:-1]) - list(reversed(said_numbers[:-1])).index(said_numbers[-1])
        said_numbers.append(current_turn-prev_spoken_index)
    current_turn += 1
print(said_numbers[-1])
