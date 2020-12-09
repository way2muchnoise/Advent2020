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
        print(port_data[pointer])
    pointer += 1
