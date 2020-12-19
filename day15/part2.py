starting_numbers = []
with open('input.txt', 'r') as f:
    line = f.readline()
    starting_numbers.extend(map(int, line[:-1].split(',')))

said_numbers = {}
current_turn = 0
last_spoken = -1
last_spoken_in_turn = -1


def store_number(number):
    global said_numbers
    last_spoken_in_turn = said_numbers[number] if number in said_numbers.keys() else -1
    said_numbers[number] = current_turn
    return number, last_spoken_in_turn


for number in starting_numbers:
    last_spoken, last_spoken_in_turn = store_number(number)
    current_turn += 1
while current_turn < 30000000:
    if last_spoken_in_turn == -1:  # never been spoken before
        last_spoken, last_spoken_in_turn = store_number(0)
    else:  # been spoken before
        last_spoken, last_spoken_in_turn = store_number(current_turn - last_spoken_in_turn - 1)
    current_turn += 1
print(last_spoken)
