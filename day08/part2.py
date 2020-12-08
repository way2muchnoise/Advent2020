def simulate_program(instruction_list):
    accumulator = 0
    executed_instructions = []
    pointer = 0

    while pointer not in executed_instructions and pointer < len(instruction_list):
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
    return accumulator, pointer


instruction_list_immutable = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        instruction_list_immutable.append(line[:-1])
        line = f.readline()

i = 0
returned_pointer = -1
returned_accumulator = -1
while i < len(instruction_list_immutable) and returned_pointer != len(instruction_list_immutable):
    instruction_list = instruction_list_immutable[:]
    if instruction_list_immutable[i][0:3] == 'nop':
        instruction_list[i] = 'jmp ' + instruction_list_immutable[i][4:]
        returned_accumulator, returned_pointer = simulate_program(instruction_list)
    elif instruction_list_immutable[i][0:3] == 'jmp':
        instruction_list[i] = 'nop ' + instruction_list_immutable[i][4:]
        returned_accumulator, returned_pointer = simulate_program(instruction_list)
    else:
        pass
    i += 1
print(returned_accumulator)
