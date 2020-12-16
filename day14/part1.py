import re

memory_pattern = re.compile(r'mem\[(\d+)] = (\d+)')


def apply_mask(value, mask):
    bin_array = list('{0:0b}'.format(int(value)))
    while len(bin_array) < len(mask):
        bin_array.insert(0, '0')
    for mask_bit_index in range(len(mask)):
        mask_bit = mask[-mask_bit_index-1]
        if mask_bit == '1' or mask_bit == '0':
            bin_array[-mask_bit_index-1] = mask_bit
    return int(''.join(bin_array), 2)


memory = {}
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        if line.startswith("mask"):
            mask = line[:-1].split(' = ')[1]
        else:
            address, value = memory_pattern.match(line[:-1]).groups()
            memory[address] = apply_mask(value, mask)
        line = f.readline()
print(sum(memory.values()))
