#!/usr/local/bin/python3

from enum import Enum

# STMT = EXPR OP EXPR
# EXPR = VAR | EXPR
# OP = * | +

class Operation(Enum):
    MUL = 1
    ADD = 2

class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/sample.txt')
        
    
    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n')
        return data

    def problem1(self):
        result = 0
        for line in self.data:
            # Need to tokenize?
            print(self.eval_expression(line))
        print(result)


    def problem2(self):
        pass

    def eval_expression(self, expr):
        if len(expr.split(' ')) == 1: return expr
        return expr

    def find_end_paren(self, expr):
        c = 1
        i = 1
        while c != 0:
            if i > len(expr): break
            if expr[i] == '(': c += 1
            if expr[i] == ')': c -= 1
            i += 1
        return i



if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()