#!/usr/local/bin/python3

values = []

with open('problem1_1.txt') as f:
    for line in f:
        values.append(int(line.strip()))

for i in range(len(values)):
    for j in range(i+1, len(values)):
        if(values[i] + values[j] == 2020):
            print(f"{values[i]} * {values[j]} = {values[i]*values[j]}")