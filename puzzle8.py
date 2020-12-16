#!/usr/local/bin/python3

import copy as copy

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n')
    return data

def does_loop(allInstructions):
    instructions = []
    i = 0
    acc = 0
    while i < len(allInstructions):
        if i in instructions:
            print(acc)
            return True
        instructions.append(i)
        cur = allInstructions[i]
        if cur[0] == 'nop':
            i += 1
            continue
        if cur[0] == 'acc':
            acc += cur[1]
            i += 1
        else:
            i += cur[1]
    print(f" No loop found: {acc} ({i})")
    return False

def problem1():
    lines = readfile('puzzle8.txt')
    allInstructions = []
    for line in lines:
        line = line.split(' ')
        allInstructions.append([line[0],int(line[1])])
    does_loop(allInstructions)

def problem2():
    lines = readfile('puzzle8.txt')
    allInstructions = []
    for line in lines:
        line = line.split(' ')
        allInstructions.append([line[0],int(line[1])])
    
    # Okay go through all
    print(f"All Instructions: {len(allInstructions)}")
    for i in range(len(allInstructions)):
        newIns = copy.deepcopy(allInstructions)
        if allInstructions[i][0] == 'nop':
            newIns[i][0] = 'jmp'
        if allInstructions[i][0] == 'jmp':
            newIns[i][0] = 'nop'
        else:
            continue
        if not does_loop(newIns):
            print(f"{i} Instruction {allInstructions[i][0]} {allInstructions[i][1]} converted to {newIns[i][0]} {newIns[i][1]}")
            return

problem1()
problem2()