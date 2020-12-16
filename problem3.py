#!/usr/local/bin/python3

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n')
    return data

def ski(data, right, down):
    index = 0
    trees = 0
    for i in range(0,len(data)-1, down):
        line = data[i]
        if line[index] == '#':
            trees += 1
        index = (index + right) % len(line)
        
    return trees

def problem1():
    lines = readfile('problem3.txt')
    print(f"Problem 1: {ski(lines, 3, 1)}")


def problem2():
    lines = readfile('problem3.txt')
    s1 = ski(lines, 1, 1)
    s2 = ski(lines, 3, 1)
    s3 = ski(lines, 5, 1)
    s4 = ski(lines, 7, 1)
    s5 = ski(lines, 1, 2)
    print(f"Problem 2: {s1} * {s2} * {s3} * {s4} * {s5} = {s1*s2*s3*s4*s5}")
    pass

problem1()
problem2()