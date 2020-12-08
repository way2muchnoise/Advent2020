values = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        values.append(int(line))
        line = f.readline()

for i in range(len(values)):
    for j in range(i, len(values)):
        for k in range(j, len(values)):
            if (values[i] + values[j] + values[k]) == 2020:
                print(values[i] * values[j] * values[k])
                exit(0)
print("Nothing found :(")
