seat_rows = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        seat_rows.append([char for char in line[:-1]])  # strip \n and split in chars
        line = f.readline()


def check_diagonal(row, seat, move_row, move_seat, seat_rows):
    check_row = row + move_row
    check_seat = seat + move_seat
    while 0 <= check_row < len(seat_rows) and 0 <= check_seat < len(seat_rows[check_row]) and seat_rows[check_row][check_seat] == '.':
        check_row += move_row
        check_seat += move_seat
    if 0 <= check_row < len(seat_rows) and 0 <= check_seat < len(seat_rows[check_row]) and seat_rows[check_row][check_seat] == '#':
        return 1
    else:
        return 0


def count_occupied_around(row, seat, seat_rows):
    occupied_around = 0
    occupied_around += check_diagonal(row, seat, -1, -1, seat_rows)  # top left
    occupied_around += check_diagonal(row, seat, -1,  0, seat_rows)  # top
    occupied_around += check_diagonal(row, seat, -1, +1, seat_rows)  # top right
    occupied_around += check_diagonal(row, seat,  0, -1, seat_rows)  # left
    occupied_around += check_diagonal(row, seat,  0, +1, seat_rows)  # right
    occupied_around += check_diagonal(row, seat, +1, -1, seat_rows)  # bottom left
    occupied_around += check_diagonal(row, seat, +1,  0, seat_rows)  # bottom
    occupied_around += check_diagonal(row, seat, +1, +1, seat_rows)  # bottom right
    return occupied_around


changes = -1
while changes != 0:
    changes = 0
    new_seat_rows = [row[:] for row in seat_rows]  # Copy array
    for row in range(len(seat_rows)):
        for seat in range(len(seat_rows[row])):
            if seat_rows[row][seat] != '.':
                occupied_around = count_occupied_around(row, seat, seat_rows)
                if seat_rows[row][seat] == '#' and occupied_around >= 5:
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
