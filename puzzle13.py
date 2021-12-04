#!/usr/local/bin/python3

with open("input/puzzle13.txt") as f:
    data = f.readlines()
available = list(map(lambda x: x if x=='x' else int(x), data[1].strip().split(',')))
idmap = {key:val for val, key in filter(lambda x: x[1]!='x', enumerate(available))}
idlist = [id for id in idmap]

step = idlist[0]
start = 0
for id in idlist[1:]:
    delta = idmap[id]
    for i in range(start,step*id,step):
        if not (i+delta)%id:
            step = step*id
            start = i    
print(start)


# find the number nearest
start_time = int(data[0])
# find the id of the bus I can take
# multiply the id by the difference between the start and
nearest_start_time = 939 - (939 % 7) + 7
alt_ids = {}
for id in idlist:
    alt_ids[id] = start_time - (start_time % id) + id
# start_time - min(times)
# find min and corresponding id
t = min(alt_ids.values())
id = list(alt_ids.keys())[list(alt_ids.values()).index(t)]

print(f"Part 1: {(t - start_time) * id}")