#!/usr/local/bin/python3

valid_passwords = 0
with open('problem2.txt') as f:
    for line in f:
        fields = line.split()
        min_occurences = int(fields[0].split('-')[0])
        max_occurences = int(fields[0].split('-')[1])
        required_char = fields[1][:-1]

        occurs = 0
        for c in fields[2]:
            if c == required_char: occurs += 1
        
        if occurs >= min_occurences and occurs <= max_occurences: valid_passwords+=1
print(f"{valid_passwords} Valid Passwords")
