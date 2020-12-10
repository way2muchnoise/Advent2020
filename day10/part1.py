adapters = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        adapters.append(int(line[:-1]))  # strip \n and cast to int
        line = f.readline()

sorted_adapters = sorted(adapters)
j1 = 0
j3 = 0
if sorted_adapters[0] == 1:
    j1 += 1
elif sorted_adapters[0] == 3:
    j3 += 1
for i in range(len(sorted_adapters)-1):
    if sorted_adapters[i+1] - sorted_adapters[i] == 1:
        j1 += 1
    elif sorted_adapters[i + 1] - sorted_adapters[i] == 3:
        j3 += 1
j3 += 1
print(j1*j3)
