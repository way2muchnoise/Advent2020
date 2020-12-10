def i_dont_know_the_math(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 7
    else:
        exit(1)


adapters = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        adapters.append(int(line[:-1]))  # strip \n and cast to int
        line = f.readline()

sorted_adapters = sorted(adapters)
sorted_adapters.insert(0, 0)
sorted_adapters.append(sorted_adapters[-1] + 3)
jolt_jumps = [3]  # start with a jump of 3 (simulates the needed 0)
possibilities = 1
pointer = 0
for i in range(1, len(sorted_adapters)):
    jolt_jumps.append(sorted_adapters[i] - sorted_adapters[i-1])
while pointer < len(jolt_jumps)-1:
    ones_between = 0
    while jolt_jumps[pointer+ones_between+1] != 3:
        ones_between += 1
    possibilities *= i_dont_know_the_math(ones_between)
    pointer += ones_between + 1
print(possibilities)
