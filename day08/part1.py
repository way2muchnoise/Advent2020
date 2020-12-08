instruction_list = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        instruction_list.append(line[:-1])
        line = f.readline()

accumulator = 0
executed_instructions = []
pointer = 0

while pointer not in executed_instructions:
    instruction = instruction_list[pointer]
    executed_instructions.append(pointer)
    if instruction[0:3] == 'nop':
        pointer += 1
    elif instruction[0:3] == 'acc':
        accumulator += int(instruction[4:])
        pointer += 1
    elif instruction[0:3] == 'jmp':
        pointer += int(instruction[4:])
    else:
        exit(1)
print(accumulator)
