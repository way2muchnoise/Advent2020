def bin_search(start, end, search, low_half, up_half):
    if len(search) == 0:
        return start
    elif search[0] == low_half:
        return bin_search(start, end-int((end-start)/2)-1, search[1:], low_half, up_half)
    elif search[0] == up_half:
        return bin_search(start+int((end-start)/2)+1, end, search[1:], low_half, up_half)


seats = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        row = line[0:7]
        col = line[7:-1]
        row_num = bin_search(0, 127, row, 'F', 'B')
        col_num = bin_search(0, 7, col, 'L', 'R')
        seat_id = row_num * 8 + col_num
        seats.append(seat_id)
        line = f.readline()
print(max(seats))
