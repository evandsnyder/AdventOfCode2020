#!/usr/local/bin/python3

class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/sample.txt')
        
    
    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n')
        return data

    def problem1(self):
        pass


    def problem2(self):
        pass

if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()