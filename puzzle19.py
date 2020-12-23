#!/usr/local/bin/python3

class Puzzle():
    def __init__(self):
        self.ruleset = {}
        self.inputs = []
        self.readfile('input/sample.txt')
        
    
    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n\n')
        
        for rule in data[0].split('\n'):
            index = rule.split(': ')[0]
            # Need to split the rules into a list of indexes..
            rules = [r.split(' ') for r in rule.split(': ')[1].split(' | ')]
            if rules[0][0] == '"a"': rules[0][0] = 'a'
            if rules[0][0] == '"b"': rules[0][0] = 'b'
            self.ruleset[index] = rules
        self.inputs = data[1].split('\n')

    def problem1(self):
        # Given an input, check that it matches rule 0...
        # Need to check each path until the whole string is checked
        # If all rules in a required ruleset fail, it is an invalid string
        valid_strs = 0
        for inp in self.inputs:
            if self.matches(inp, self.ruleset["0"]):
                valid_strs += 1
        print(f"Part 1: {valid_strs} strings match rule 0")

    def problem2(self):
        pass

    def matches(self, string, requirements, index=0):
         print(f"Checking {string} matches: {requirements}")
         for ruleset in requirements:
            # must match at least 1 rule in ruleset
            valid = False
            for rule in ruleset:
                # Must match all rules in rule
                if rule == 'a' or rule == 'b':
                    valid = string[index] == rule
                    index += 1
                if valid:
                    self.matches(string, self.ruleset[rule], index)
            if not valid:
                continue

if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()