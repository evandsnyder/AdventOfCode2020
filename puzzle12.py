#!/usr/local/bin/python3

class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/puzzle12.txt')
    
    def readfile(self, file):
        data = []
        with open(file) as f:
            for line in f:
                data.append((line[0],int(line.rstrip()[1:])))
        return data

    def problem1(self):
        # Find manhattan distance after instructions processed
        # Boat starts facing east
        x = 0
        y = 0
        facing = "E"
        self.angle = 90
        for ins in self.data:
            op = ins[0]
            dis = ins[1]
            if op == 'N' or (op == 'F' and facing == 'N'):
                y += dis
            if op == 'E' or (op == 'F' and facing == 'E'):
                x += dis
            if op == 'S' or (op == 'F' and facing == 'S'):
                y -= dis
            if op == 'W' or (op == 'F' and facing == 'W'):
                x -= dis
            if op == 'R' or op == 'L':
                facing = self.update_direction(op, dis)
        print(f"({x}, {y})")
        print(abs(x) + abs(y))


    def problem2(self):
        ship_x = 0
        ship_y = 0
        waypoint_x = 10
        waypoint_y = 1
        for ins in self.data:
            # print(f"({ship_x}, {ship_y}) : ({waypoint_x}, {waypoint_y})")
            op = ins[0]
            dis = ins[1]
            if op == 'N':
                waypoint_y += dis
            if op == 'E':
                waypoint_x += dis
            if op == 'S':
                waypoint_y -= dis
            if op == 'W':
                waypoint_x -= dis
            if op == 'R' or op == 'L':
                waypoint_x, waypoint_y = self.translate_waypoint(op, dis, waypoint_x, waypoint_y)
            if op == 'F':
                ship_x += dis*waypoint_x
                ship_y += dis*waypoint_y
        # print(f"({ship_x}, {ship_y}) : ({waypoint_x}, {waypoint_y})")
        print(abs(ship_x) + abs(ship_y))

    def update_direction(self, op, dis):
        if op == 'L':
            self.angle = (self.angle - dis) % 360
        else:
            self.angle = (self.angle + dis) % 360
        
        if self.angle == 360 or self.angle == 0:
            self.angle = 0
            return 'N'
        
        if self.angle == -90 or self.angle == 270:
            self.angle = 270
            return 'W'
        
        if self.angle == 90:
            return 'E'
        
        if self.angle == 180:
            return 'S'
        
        return None
    
    def translate_waypoint(self, op, dis, x, y):
        print(f"Translating by {op}{dis}")
        if op == 'R':
            for i in range(self.angle, self.angle + dis, 90):
                x,y = y,-x
            # Normalize angle...
            self.angle = (self.angle + dis) % 360
            return x,y
        
        for i in range(self.angle, self.angle - dis, -90):
                x, y = -y, x
        self.angle = (self.angle - dis) % 360
        return x, y

if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()