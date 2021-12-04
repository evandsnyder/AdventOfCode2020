#!/usr/local/bin/python3

import re


class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/puzzle14.txt')

    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n')
        return data

    def problem1(self):
        mask = ''
        memory = dict()
        for line in self.data:
            if 'mask = ' in line:
                mask = line.split()[-1]
            else:
                # gotta get the memory address and the mask...
                elements = line.split()
                address = elements[0][4:-1]
                # Convert integer to binary
                # prepend with 0s...
                value = bin(int(elements[-1]))[2:].zfill(36)


                # Apply the mask to the value...
                masked_value = [value[i] for i in range(len(value))]
                for i in range(len(mask)):
                    if mask[i] != 'X':
                        masked_value[i] = mask[i]
                # Store it in the memory
                memory[address] = ''.join(masked_value)
        
        # Okay, iterate over the values! conver them to ints and sum them up
        result = 0
        for v in memory.values():
            result += int(v, 2)
        
        print(result)

    def problem2(self):
        pass


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()
