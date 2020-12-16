#!/usr/local/bin/python3

valid_passwords = 0
with open('problem2.txt') as f:
    for line in f:
        fields = line.split()
        first_pos = int(fields[0].split('-')[0])-1
        sec_pos = int(fields[0].split('-')[1])-1
        required_char = fields[1][:-1]

        if bool(fields[2][first_pos] == required_char) != bool(fields[2][sec_pos] == required_char):
            valid_passwords += 1
        
print(f"{valid_passwords} Valid Passwords")
