import re

range_pattern = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')

absolute_min_min = 1000
absolute_min_max = 0
absolute_max_min = 1000
absolute_max_max = 0
other_tickets = []
with open('input.txt', 'r') as f:
    line = f.readline()
    line_count = 0
    while line and line_count < 20:
        min_min, min_max, max_min, max_max = map(int, range_pattern.search(line).groups())
        absolute_min_min = min_min if min_min < absolute_min_min else absolute_min_min
        absolute_min_max = min_max if min_max > absolute_min_max else absolute_min_max
        absolute_max_min = max_min if max_min < absolute_max_min else absolute_max_min
        absolute_max_max = max_max if max_max > absolute_max_max else absolute_max_max
        line = f.readline()
        line_count += 1
    line = f.readline()  # skip blank line
    line = f.readline()  # skip "your ticket" line
    line = f.readline()  # skip your ticket
    line = f.readline()  # skip blank line
    line = f.readline()  # skip "nearby tickets" line
    while line:
        other_tickets.append(list(map(int, line[:-1].split(','))))
        line = f.readline()


def is_valid_number(number):
    return absolute_min_min <= number <= absolute_min_max or absolute_max_min <= number <= absolute_max_max


invalid_tickets = 0
for ticket in other_tickets:
    checked_numbers = 0
    while checked_numbers < len(ticket) and is_valid_number(ticket[checked_numbers]):
        checked_numbers += 1
    if checked_numbers != len(ticket):
        invalid_tickets += ticket[checked_numbers]
print(invalid_tickets)
