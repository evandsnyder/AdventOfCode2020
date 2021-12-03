#!/usr/local/bin/python3

class Number():
    def __init__(self, num, first_turn_spoken):
        self.number = num
        self.prev_turn = first_turn_spoken
        self.prev_prev_turn = -1
    
    def update_last_said(self, turn):
        self.prev_prev_turn = self.prev_turn
        self.prev_turn = turn
        r = self.prev_turn - self.prev_prev_turn
        # print(f"\t{self.prev_turn} - {self.prev_prev_turn} = {r}")
        return r


class Puzzle():
    def __init__(self):
        # self.data = {20: 1, 0: 2, 1: 3, 11: 4, 6: 5, 3: 6}
        # self.data = {0: Number(0, 1), 3: Number(3,2), 6: Number(6, 3)}
        self.data = {}
        # 14,1,17,0,3,20

        for i, v in enumerate([14,1,17,0,3,20]):
            self.data[v] = Number(v, i+1)


    
    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n')
        return data

    def problem1(self):
        last_said = 0
        i = len(self.data.keys())+1
        while i < 30000000:
            # print(f"({i}) Last Said: {last_said}")
            if last_said in self.data.keys():
                # said becomes last_said - i
                # Need to update dictionary with new turn value
                last_said = self.data[last_said].update_last_said(i)
            else:
                self.data[last_said] = Number(last_said, i)
                last_said = 0
            i += 1
        print(last_said)


    def problem2(self):
        pass

if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()