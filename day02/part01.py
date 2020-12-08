def check_policy(min, max, letter, password):
    letter_count = password.count(letter)
    return int(min) <= letter_count <= int(max)


valid_passwords = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        min_max, letter, password = line.split(" ")
        min, max = min_max.split("-")
        letter = letter[:-1]  # remove :
        password = password[:-1]  # remove \n
        if check_policy(min, max, letter, password):
            valid_passwords = valid_passwords + 1
        line = f.readline()
print(valid_passwords)
