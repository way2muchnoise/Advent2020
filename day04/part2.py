import re

hair_colour = re.compile(r'^#[0-9a-f]{6}$')
passport_id = re.compile(r'^\d{9}$')

def parse_passport(lines):
    passport = {}
    for line in lines:
        for kv in line[:-1].split(' '):
            k, v = kv.split(':')
            passport[k] = v
    return passport


def is_valid_heigth(hgt):
    number = hgt[0:-2]
    unit = hgt[-2:]
    if unit == 'cm':
        return 150 <= int(number) <= 193
    elif unit == 'in':
        return 59 <= int(number) <= 76
    else:
        return False


def is_valid(passport):
    passport_keys = passport.keys()
    return  'byr' in passport_keys and 1920 <= int(passport['byr']) <= 2002 and \
            'iyr' in passport_keys and 2010 <= int(passport['iyr']) <= 2020 and \
            'eyr' in passport_keys and 2020 <= int(passport['eyr']) <= 2030 and \
            'hgt' in passport_keys and is_valid_heigth(passport['hgt']) and\
            'hcl' in passport_keys and hair_colour.match(passport['hcl']) and \
            'ecl' in passport_keys and passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and \
            'pid' in passport_keys and passport_id.match(passport['pid'])


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
