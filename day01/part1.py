values = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        values.append(int(line))
        line = f.readline()

for i in range(len(values)):
    for j in range(i, len(values)):
        if (values[i] + values[j]) == 2020:
            print(values[i] * values[j])
            exit(0)
print("Nothing found :(")
