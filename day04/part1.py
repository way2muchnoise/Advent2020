def parse_passport(lines):
    passport = {}
    for line in lines:
        for kv in line[:-1].split(' '):
            k, v = kv.split(':')
            passport[k] = v
    return passport


def is_valid(passport):
    passport_keys = passport.keys()
    return  'byr' in passport_keys and \
            'iyr' in passport_keys and \
            'eyr' in passport_keys and \
            'hgt' in passport_keys and \
            'hcl' in passport_keys and \
            'ecl' in passport_keys and \
            'pid' in passport_keys


passport_count = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    passport_lines = []
    while line:
        if line == "\n" or line == '':
            passport = parse_passport(passport_lines)
            if is_valid(passport):
                passport_count += 1
            passport_lines = []
        else:
            passport_lines.append(line)
        line = f.readline()
print(passport_count)
