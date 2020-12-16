#!/usr/local/bin/python3

class Child:
    def __init__(self, count, color):
        self.color = color
        self.count = count
        self.parents = []
    
    def addParent(self, parent):
        self.parents.append(parent)
    
    def __str__(self):
        return f"{self.count} {self.color}"

def checkParent(color, allBags, checked):
    if color in checked:
        return 0
    checked.append(color)
    if not color in allBags: return 1
    total = 1
    for parent in allBags[color]:
        total += checkParent(parent, allBags, checked)
    return total

def countChildren(child, allBags):
    total = 1
    for c in allBags[child.color]:
        total += countChildren(c, allBags)
    return total * child.count

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n')
    return data

def problem1():
    lines = readfile('problem7.txt')
    bags = dict()
    for line in lines:
        line = line[:-1] # Remove .
        data = line.split(" contain ")
        parent = data[0][:-5]
        bags[parent] = []
        if(data[1] == 'no other bags'):
            continue
        children = data[1].split(', ')
        for child in children:
            child = child.replace('bags', '').replace('bag', '')
            c = Child(int(child[0]), child[2:-1])
            bags[parent].append(c)
    
    # We now have a dictionary where key = parents and v = list of children
    # Need to invert that so we have a dictionary of bags with all of their parents
    children = dict()
    for key in bags:
        for bag in bags[key]:
            if(not bag.color in children):
                children[bag.color] = []
            children[bag.color].append(key)
    # Find all parents of shiny gold
    total = len(children["shiny gold"])
    print(checkParent("shiny gold", children, [])-1)

def problem2():
    lines = readfile('problem7.txt')
    bags = dict()
    for line in lines:
        line = line[:-1] # Remove .
        data = line.split(" contain ")
        parent = data[0][:-5]
        bags[parent] = []
        if(data[1] == 'no other bags'):
            continue
        children = data[1].split(', ')
        for child in children:
            child = child.replace('bags', '').replace('bag', '')
            c = Child(int(child[0]), child[2:-1])
            bags[parent].append(c)
    # for each child in 
    total = 0
    for child in bags["shiny gold"]:
        total += countChildren(child, bags)
    print(total)

problem1()
problem2()