#!/usr/local/bin/python3

class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/puzzle1.txt')

    def readfile(self, file):
        data = []
        with open('input/puzzle1.txt') as f:
            for line in f:
                data.append(int(line.strip()))
        return data

    def problem1(self):
        for i in range(len(self.data)):
            for j in range(i+1, len(self.data)):
                if(self.data[i] + self.data[j] == 2020):
                    print(f"{self.data[i]} * {self.data[j]} = {self.data[i]*self.data[j]}")

    def problem2(self):

        for i in range(len(self.data)):
            for j in range(i+1, len(self.data)):
                for k in range(j+1, len(self.data)):
                    if(self.data[i] + self.data[j] + self.data[k] == 2020):
                        print(
                            f"{self.data[i]} * {self.data[j]} * {self.data[k]} = {self.data[i]*self.data[j]*self.data[k]}")


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()
