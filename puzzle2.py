#!/usr/local/bin/python3

class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/puzzle2.txt')

    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n')
        return data

    def problem1(self):
        valid_passwords = 0
        for line in self.data:
            fields = line.split()
            min_occurences = int(fields[0].split('-')[0])
            max_occurences = int(fields[0].split('-')[1])
            required_char = fields[1][:-1]

            occurs = 0
            for c in fields[2]:
                if c == required_char:
                    occurs += 1

            if occurs >= min_occurences and occurs <= max_occurences:
                valid_passwords += 1
        print(f"{valid_passwords} Valid Passwords")

    def problem2(self):
        valid_passwords = 0
        for line in self.data:
            fields = line.split()
            first_pos = int(fields[0].split('-')[0])-1
            sec_pos = int(fields[0].split('-')[1])-1
            required_char = fields[1][:-1]

            if bool(fields[2][first_pos] == required_char) != bool(fields[2][sec_pos] == required_char):
                valid_passwords += 1
        print(f"{valid_passwords} Valid Passwords")


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()
