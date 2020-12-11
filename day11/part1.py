seat_rows = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        seat_rows.append([char for char in line[:-1]])  # strip \n and split in chars
        line = f.readline()


def count_occupied_around(row, seat, seat_rows):
    occupied_around = 0
    if row-1 >= 0:
        if seat-1 >= 0 and seat_rows[row-1][seat-1] == '#':  # top left
            occupied_around += 1
        if seat_rows[row-1][seat] == '#':  # top
            occupied_around += 1
        if seat+1 < len(seat_rows[row-1]) and seat_rows[row-1][seat+1] == '#':  # top right
            occupied_around += 1
    if seat-1 >= 0 and seat_rows[row][seat-1] == '#':  # left
        occupied_around += 1
    if seat+1 < len(seat_rows[row]) and seat_rows[row][seat+1] == '#':  # right
        occupied_around += 1
    if row+1 < len(seat_rows):
        if seat-1 >= 0 and seat_rows[row+1][seat-1] == '#':  # bottom left
            occupied_around += 1
        if seat_rows[row+1][seat] == '#':  # bottom
            occupied_around += 1
        if seat+1 < len(seat_rows[row+1]) and seat_rows[row+1][seat+1] == '#':  # bottom right
            occupied_around += 1
    return occupied_around


changes = -1
while changes != 0:
    changes = 0
    new_seat_rows = [row[:] for row in seat_rows]  # Copy array
    for row in range(len(seat_rows)):
        for seat in range(len(seat_rows[row])):
            if seat_rows[row][seat] != '.':
                occupied_around = count_occupied_around(row, seat, seat_rows)
                if seat_rows[row][seat] == '#' and occupied_around >= 4:
                    new_seat_rows[row][seat] = 'L'
                    changes += 1
                if seat_rows[row][seat] == 'L' and occupied_around == 0:
                    new_seat_rows[row][seat] = '#'
                    changes += 1
    seat_rows = new_seat_rows
occupied = 0
for row in seat_rows:
    for seat in row:
        if seat == '#':
            occupied += 1
print(occupied)
