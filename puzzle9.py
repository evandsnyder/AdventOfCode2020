#!/usr/local/bin/python3

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n')
    return [int(x) for x in data[:-1]]

def checkHistory(target, arr):
    for i, num in enumerate(arr[:-1]):
        if target - num in arr[i+1:]:
            return True
    return False

def problem1(lines):
    for i in range(26, len(lines)):
        if not checkHistory(lines[i], lines[i-26:i]):
            print(f"Failed to validate: {lines[i]}")
            break

def problem2(lines):
    magic_number = 177777905
    # find stuff that adds up to this...
    for i, n in enumerate(lines):
        # Add all from [i:]
        j = i+1
        s = n
        while s <= magic_number:
            s += lines[j]
            if s == magic_number:
                print(f"{min(lines[i:j+1]) + max(lines[i:j+1])}")
                break
            j += 1

data = readfile('input/puzzle9.txt')
problem1(data)
problem2(data)