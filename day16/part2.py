import re

range_pattern = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')

absolute_min_min = 1000
absolute_min_max = 0
absolute_max_min = 1000
absolute_max_max = 0
other_tickets = []
valid_ranges = []
your_ticket = []
ticket_fields = [
    'departure location', 'departure station', 'departure platform', 'departure track', 'departure date',
    'departure time',
    'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'duration', 'price', 'route',
    'row', 'seat', 'train', 'type', 'wagon', 'zone']
with open('input.txt', 'r') as f:
    line = f.readline()
    line_count = 0
    while line and line_count < 20:
        min_min, min_max, max_min, max_max = map(int, range_pattern.search(line).groups())
        valid_ranges.append((min_min, min_max, max_min, max_max))
        absolute_min_min = min_min if min_min < absolute_min_min else absolute_min_min
        absolute_min_max = min_max if min_max > absolute_min_max else absolute_min_max
        absolute_max_min = max_min if max_min < absolute_max_min else absolute_max_min
        absolute_max_max = max_max if max_max > absolute_max_max else absolute_max_max
        line = f.readline()
        line_count += 1
    line = f.readline()  # skip blank line
    line = f.readline()  # skip "your ticket" line
    your_ticket = list(map(int, line[:-1].split(',')))
    line = f.readline()  # skip blank line
    line = f.readline()  # skip "nearby tickets" line
    line = f.readline()
    while line:
        other_tickets.append(list(map(int, line[:-1].split(','))))
        line = f.readline()


def is_valid_number(number,
                    min_min=absolute_min_min, min_max=absolute_min_max,
                    max_min=absolute_max_min, max_max=absolute_max_max):
    return min_min <= number <= min_max or max_min <= number <= max_max


valid_tickets = []
for ticket in other_tickets:
    checked_numbers = 0
    while checked_numbers < len(ticket) and is_valid_number(ticket[checked_numbers]):
        checked_numbers += 1
    if checked_numbers == len(ticket):
        valid_tickets.append(ticket)

possible_fields_for_valid_ranges = []
for valid_range in valid_ranges:
    possible_fields = set(range(len(valid_ranges)))
    t = 0
    for ticket in valid_tickets:
        invalid_fields = []
        for position in possible_fields:
            if not is_valid_number(ticket[position], *valid_range):
                invalid_fields.append(position)
        possible_fields.difference_update(invalid_fields)
    possible_fields_for_valid_ranges.append(possible_fields)
field_mapping = {}
for i in range(len(ticket_fields)):
    field_mapping[ticket_fields[i]] = possible_fields_for_valid_ranges[i]

while sum(map(len, field_mapping.values())) > len(ticket_fields):
    for ticket_field in ticket_fields:
        if len(field_mapping[ticket_field]) == 1:
            only_field = list(field_mapping[ticket_field])[0]
            [mapped_field.discard(only_field) for mapped_field in field_mapping.values()]
            field_mapping[ticket_field].add(only_field)
departure_multiplication = 1
for ticket_field in ticket_fields:
    if ticket_field.startswith('departure'):
        departure_multiplication *= your_ticket[list(field_mapping[ticket_field])[0]]
print(departure_multiplication)
