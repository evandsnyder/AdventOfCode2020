#!/usr/local/bin/python3

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n\n')
    return data

def problem1():
    lines = readfile('input/Problem6.txt')
    total = 0
    for group in lines:
        string = group.replace('\n','').replace('\r', '').replace('\t', '')
        total += len(set(string))

    print(f"{total}")


def problem2():
    lines = readfile('input/Problem6.txt')
    total = 0
    for group in lines:
        info = group.split('\n')
        # have list where each entry is one person
        # Must find all shared characters in every entry
        shared = ''.join(set(info[0]))
        for person in info:
            # print(f"comparing {person} and {shared}")
            shared = ''.join(set(shared).intersection(person))
        total += len(shared)

    print(total)

problem1()
problem2()