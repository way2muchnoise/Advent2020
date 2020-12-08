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


def get_bag_count_recursive(colour, count=1):
    if count == 0:
        return 0
    contents = bag_map[colour]
    total_count = sum([get_bag_count_recursive(content[1], content[0]) for content in contents])
    return total_count * count + count


print(get_bag_count_recursive('shiny gold') - 1)  # -1 since we don't count the shiny gold bag
