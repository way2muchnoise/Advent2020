port_data = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        port_data.append(int(line[:-1]))  # strip \n and cast to int
        line = f.readline()

preamble_size = 25
pointer = preamble_size
while pointer < len(port_data):
    number_set = port_data[pointer-preamble_size:pointer]
    sum_set = set()
    for i in range(len(number_set)):
        for j in range(i, len(number_set)):
            sum_set.add(number_set[i] + number_set[j])
    if port_data[pointer] not in sum_set:
        invalid_number = port_data[pointer]
        contiguous_sum = 0
        contiguous_pointer = 0
        contiguous_size = 0
        while contiguous_sum != invalid_number:
            if contiguous_sum > invalid_number:
                contiguous_pointer += 1
                contiguous_size = 0
                contiguous_sum = 0
            else:
                contiguous_sum += port_data[contiguous_pointer+contiguous_size]
                contiguous_size += 1
        print(min(port_data[contiguous_pointer:contiguous_pointer+contiguous_size]) +
              max(port_data[contiguous_pointer:contiguous_pointer+contiguous_size]))
    pointer += 1
