def parse_rule(rule):
    bag, contents = rule[:-2].split('contain ')  # Remove \n and .
    bag = ' '.join(bag.split(' ')[:2])
    contents = contents.split(', ')
    for i in range(len(contents)):
        count, colour = contents[i].split(' ', 1)
        colour = ' '.join(colour.split(' ')[:2])
        count = 0 if count == 'no' else int(count)
        contents[i] = (count, colour)
    return bag, contents


bag_map = {}
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        bag, contents = parse_rule(line)
        bag_map[bag] = contents
        line = f.readline()

can_carry = ['shiny gold']
can_carry_immutable = []
while len(can_carry) > 0:
    find = can_carry.pop()
    for bag_key in bag_map:
        if find in [content[1] for content in bag_map[bag_key]]:
            can_carry.append(bag_key)
            can_carry_immutable.append(bag_key)
print(len(set(can_carry_immutable)))
