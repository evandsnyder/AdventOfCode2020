#!/usr/local/bin/python3

import copy as copy

class Puzzle():
    def __init__(self):
        self.readfile('input/puzzle11.txt')
    
    def readfile(self, file):
        self.data = []
        with open(file) as f:
            for line in f:
                self.data.append([c for c in line.rstrip()])

    def problem1(self):
        self.simulate()
        # Count occupied seats
        print(sum([i.count('#') for i in self.data]))

    def problem2(self):
        self.readfile('input/puzzle11.txt')
        next_frame = copy.deepcopy(self.data)
        seats_changed = True
        while(seats_changed):
            seats_changed = False
            for i, e in enumerate(self.data):
                for j, v in enumerate(e):
                    if v == '.': continue
                    surroundings = self.count_visible(i, j)
                    # print(f"SURROUNDINGS: {surroundings}")
                    if v == 'L' and surroundings == 0:
                        seats_changed = True
                        next_frame[i][j] = '#'
                    elif v == '#' and surroundings >= 5:
                        seats_changed = True
                        next_frame[i][j] = 'L'
            self.data = copy.deepcopy(next_frame)
            for i in self.data:
                print(''.join(i))
            print("")
        print(sum([i.count('#') for i in self.data]))
    
    def simulate(self):
        next_frame = copy.deepcopy(self.data)
        seats_changed = True
        m = 0
        while(seats_changed):
            seats_changed = False
            for i, e in enumerate(self.data):
                for j, v in enumerate(e):
                    if v == '.': continue
                    surroundings = self.count_surrounding(i, j)
                    # print(f"SURROUNDINGS: {surroundings}")
                    if v == 'L' and surroundings == 0:
                        seats_changed = True
                        next_frame[i][j] = '#'
                    elif v == '#' and surroundings >= 4:
                        seats_changed = True
                        next_frame[i][j] = 'L'
            self.data = copy.deepcopy(next_frame)
            for i in self.data:
                print(''.join(i))
            print("")
            m += 1
    
    def count_surrounding(self, i, j, value='#'):
        # Need to make sure i and j do not violate bounds of array...
        m_i = len(self.data)-1
        m_j = len(self.data[i])-1
        count = 0
        count += (1 if i > 0   and j > 0 and self.data[i-1][j-1] == value else 0)
        count += (1 if i > 0   and self.data[i-1][j]   == value else 0)
        count += (1 if i > 0   and j < m_j and self.data[i-1][j+1] == value else 0)
        count += (1 if j > 0   and self.data[i][j-1]   == value else 0)
        count += (1 if j < m_j and self.data[i][j+1]   == value else 0)
        count += (1 if i < m_i and j > 0 and self.data[i+1][j-1] == value else 0)
        count += (1 if i < m_i and self.data[i+1][j]   == value else 0)
        count += (1 if i < m_i and j < m_j and self.data[i+1][j+1] == value else 0)
        return count
    
    def count_visible(self, i, j, value='#'):
        m_i = len(self.data)-1
        m_j = len(self.data[i])-1
        m = i
        n = j
        count = 0
        # Check N
        while(m > 0 and self.data[m-1][j] == '.'):
            m -= 1
        count += (1 if m > 0 and self.data[m-1][j] == value else 0)
        m = i
        # Check NE
        while(m > 0 and n < m_j and self.data[m-1][n+1] == '.'):
            m -= 1
            n += 1
        count += (1 if m > 0 and n < m_j and self.data[m-1][n+1] == value else 0)
        m = i
        n = j
        # Check E
        while n < m_j and self.data[i][n+1] == '.':
            n += 1
        count += (1 if n < m_j and self.data[i][n+1] == value else 0)
        n = j
        # Check SE
        while m < m_i and n < m_j and self.data[m+1][n+1] == '.':
            n += 1
            m += 1
        count += (1 if m < m_i and n < m_j and self.data[m+1][n+1] == value else 0)
        n = j
        m = i
        # Check S
        while(m < m_i and self.data[m+1][j] == '.'):
            m += 1
        count += (1 if m < m_i and self.data[m+1][j] == value else 0)
        m = i
        # Check SW
        while m < m_i and n > 0 and self.data[m+1][n-1] == '.':
            m += 1
            n -= 1
        count += (1 if m < m_i and n > 0 and self.data[m+1][n-1] == value else 0)
        m = i
        n = j
        # Check W
        while(n > 0 and self.data[i][n-1] == '.'):
            n -= 1
        count += (1 if n > 0 and self.data[i][n-1] == value else 0)
        n = j
        # Check NW
        while m > 0 and n > 0 and self.data[m-1][n-1] == '.':
            n -= 1
            m -=1
        count += (1 if n > 0 and m > 0 and self.data[m-1][n-1] == value else 0)
        return count


if __name__ == '__main__':
    puzzle = Puzzle()
    # puzzle.problem1()
    puzzle.problem2()