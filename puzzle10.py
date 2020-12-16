#!/usr/local/bin/python3

def gen_tribonnaci(n):
    if n < 3 : return 0
    if n == 3: return 1
    return gen_tribonnaci(n-1) + gen_tribonnaci(n-2) + gen_tribonnaci(n-3)

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n')
    return [int(x) for x in data[:-1]]

def problem1(lines):
    lines.append(0)
    lines.sort()
    lines.append(lines[-1]+3)
    res = [0, 0, 0, 0]
    for i in range(len(lines)-1):
        res[lines[i+1]-lines[i]] += 1
    print(f"Problem 10 Part 1: {res[1] * res[3]}")


def problem2(lines):
    diffs = [lines[i+1]-lines[i] for i in range(len(lines)-1)]
    trib = [gen_tribonnaci(n) for n in range(3, 21)]
    permutations = 1
    ones = 0
    for n in diffs:
        if n == 1:
            ones += 1
        else:
            permutations  *= trib[ones]
            ones = 0
    print(permutations)

data = readfile('input/puzzle10.txt')
problem1(data)
problem2(data)