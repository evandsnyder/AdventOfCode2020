#!/usr/local/bin/python3
from queue import Queue

class Puzzle():
    def __init__(self):
        self.player1 = Queue()
        self.player2 = Queue()
        self.readfile('input/Problem22.txt')
        
    
    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n\n')
        for x in data[0].split('\n')[1:]:
            self.player1.put(int(x))
        for x in data[1].split('\n')[1:-1]:
            self.player2.put(int(x))

    def problem1(self):
        while not self.player1.empty() and not self.player2.empty():
            # Playing round
            p1_card = self.player1.get()
            p2_card = self.player2.get()

            if p1_card > p2_card:
                self.player1.put(p1_card)
                self.player1.put(p2_card)
            else:
                self.player2.put(p2_card)
                self.player2.put(p1_card)
        
        w = self.player2
        if not self.player1.empty():
            w = self.player1
        
        winner = []
        while not w.empty():
            winner = [w.get()] + winner
        
        print(f"WINNER: {winner}")
        result = 0
        for i, n in enumerate(winner):
            result += (i+1) * n
        print(f"result: {result}")


    def problem2(self):
        pass

if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()