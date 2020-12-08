def check_policy(pos1, pos2, letter, password):
    return (password[int(pos1)-1] == letter) ^ (password[int(pos2)-1] == letter)  # XOR

valid_passwords = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        positions, letter, password = line.split(" ")
        pos1, pos2 = positions.split("-")
        letter = letter[:-1]  # remove :
        password = password[:-1]  # remove \n
        if check_policy(pos1, pos2, letter, password):
            valid_passwords = valid_passwords + 1
        line = f.readline()
print(valid_passwords)
