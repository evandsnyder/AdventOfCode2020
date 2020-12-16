#!/usr/local/bin/python3

class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.seat_id = row*8 + col

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n')
    return data[:-1]

def problem1():
    lines = readfile('problem5.txt')
    #lines = ["FBFBBFFRLR"]
    seat_ids = []
    seats = []
    for line in lines:
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7
        for c in line:
            # FBFBBFFRLR
            # Find midpoint..
            # ((max_row - min_row) // 2) + min_row
            mid_row = -(-(max_row - min_row) // 2) + min_row
            mid_col = -(-(max_col - min_col) // 2) + min_col
            if c == 'F':
                max_row = mid_row-1
            if c == 'B':
                min_row = mid_row
            if c == 'L':
                max_col = mid_col-1
            if c == 'R':
                min_col = mid_col
        seats.append(Seat(max_row, max_col))
        seat_ids.append((max_row*8) + max_col)
    print(max(seat_ids))
    seat_ids.sort()
    print(seat_ids)
    for i in range(len(seat_ids)-2):
        j = i+1
        if seat_ids[j] - seat_ids[i] == 2:
            print(f"Potential: {seat_ids[i]} {seat_ids[j]} : {seat_ids[i]+1}")



def problem2():
    lines = readfile('problem5.txt')
    pass

problem1()
problem2()

# aaabaaa
"""
aaa
aa
 aa
bxaaabx
aaabxbx
([a-z]{2})\\1
"""
