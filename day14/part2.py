import re

memory_pattern = re.compile(r'mem\[(\d+)] = (\d+)')


def generate_permutations(masked_array):
    permutations = []
    significant_bit = masked_array[0]
    significant_bit_permutations = []
    if significant_bit == 'X':
        significant_bit_permutations.append('0')
        significant_bit_permutations.append('1')
    else:
        significant_bit_permutations.append(significant_bit)
    if len(masked_array) == 1:
        permutations = significant_bit_permutations
    else:
        remaining_mask = masked_array[1:]
        remaining_permutations = generate_permutations(remaining_mask)
        for significant_bit_permutation in significant_bit_permutations:
            for remaining_permutation in remaining_permutations:
                permutation = [significant_bit_permutation]
                permutation.extend(remaining_permutation)
                permutations.append(permutation)
    return permutations


def apply_mask(memory, mask):
    bin_array = list('{0:0b}'.format(int(memory)))
    while len(bin_array) < len(mask):
        bin_array.insert(0, '0')
    for mask_bit_index in range(len(mask)):
        mask_bit = mask[-mask_bit_index-1]
        if mask_bit != '0':
            bin_array[-mask_bit_index-1] = mask_bit
    return map(lambda permutation: int(''.join(permutation), 2), generate_permutations(bin_array))


memory = {}
mask = '000000000000000000000000000000000000'
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        if line.startswith("mask"):
            mask = line[:-1].split(' = ')[1]
        else:
            address, value = memory_pattern.match(line[:-1]).groups()
            for mem_address in apply_mask(address, mask):
                memory[mem_address] = int(value)
        line = f.readline()
print(sum(memory.values()))
