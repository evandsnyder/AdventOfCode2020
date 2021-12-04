#!/usr/local/bin/python3

from enum import Enum

# STMT = EXPR OP EXPR | STMT | EXPR
# EXPR = VAR | EXPR
# OP = * | +

# How to do an AST?

class Expression():
    data: any

class Statment():
    operand: str
    left_hand_side: Expression = None
    right_hand_side: Expression = None


class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/puzzle18.txt')

    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n')
        return data

    def problem1(self):
        result = 0
        for line in self.data:
            # Need to tokenize?
            result += self.evaluate_expression(line)
        print(result)

    def problem2(self):
        pass

    def parse_expression():
        pass

    def evaluate_expression(self, expression: str):
        # if this is a variable, get next operand, and expression to the right...
        # For char in expression..
        if len(expression) == 0:
            return 0
        expression = expression.strip()
        if ' ' not in expression:
            return int(expression)
        

        lhs: int = 0
        rhs: int = 0

        op_index: int

        if expression[0] == '(':
            op_index = self.find_matching_parentheses(expression, 0)

            lhs = self.evaluate_expression(expression[1:op_index])
            # Maybe consume the token... ?
            # The new expression will be:
            expression = expression[op_index + 2:]
        else:
            # Seek from 0: first whitespace...
            index_of_whitespace = 1
            for i in range(len(expression)):
                if expression[i] == ' ':
                    index_of_whitespace = i
                    break
            lhs = int(expression[0:index_of_whitespace])
            expression = expression[index_of_whitespace+1:]

        operand = expression[0]
        expression = expression[2:]

        if expression[0] == '(':
            end_index = self.find_matching_parentheses(expression, 0)
            rhs = self.evaluate_expression(expression[1:end_index])
            expression = expression[end_index + 2:]
        else:
            index_of_whitespace = 1
            for i in range(len(expression)):
                if expression[i] == ' ':
                    index_of_whitespace = i
                    break
            rhs = int(expression[0:index_of_whitespace])
            expression = expression[index_of_whitespace + 1:]

        result: int = 0

        if operand == '+':
            result = lhs + rhs
        else:
            result = lhs * rhs

        new_expr = f"{result} {expression}"

        return self.evaluate_expression(new_expr)

    def find_matching_parentheses(self, expression: str, start_index: int) -> int:
        # Return end index
        end_index: int = start_index
        depth = 1
        while depth > 0:
            end_index += 1
            if expression[end_index] == ')':
                depth -= 1
            if expression[end_index] == '(':
                depth += 1
        return end_index


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()
