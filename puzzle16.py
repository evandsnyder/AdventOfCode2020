#!/usr/local/bin/python3
import constraint

def invalid_ticket(ticket, constraints):
    problem = constraint.Problem()
    problem.addVariable('x', ticket)
    for c in constraints: problem.addConstraint(c)
    return len(problem.getSolutions()) > 0

class Puzzle():
    def __init__(self):
        self.data = self.readfile('input/puzzle16.txt')
        self.requirements = self.data[0]
        self.your_ticket = self.data[1]
        self.nearby = self.data[2]
    
    def readfile(self, file):
        data = []
        with open(file) as f:
            data = f.read().split('\n\n')
        return data

    def problem1(self):
        nearby = []
        for line in self.nearby.split('\n')[1:]:
            nearby = nearby + [int(x) for x in line.split(',')] 
        problem = constraint.Problem()
        problem.addVariable('x', nearby)
        
        for req in self.requirements.split('\n'):
            req = req.split(': ')
            req = req[1].split(' or ')
            for r in req:
                r = r.split('-')
                problem.addConstraint(lambda x, y=int(r[0]), z=int(r[1]): x if not y <= x <= z else 0 , ['x'])
        ans = 0
        for d in problem.getSolutions():
            ans += d['x']
        print(ans)


    def problem2(self):
        tickets = []
        for line in self.nearby.split('\n')[1:]:
            tickets.append([int(x) for x in line.split(',')])
        empty_ticket = [None] * len(tickets[0])
        constraints = []
        valid_constraints = dict()
        for req in self.requirements.split('\n'):
            req = req.split(': ')
            field = req[0]
            req = req[1].split(' or ')
            y = z = a = b = 0

            # Create constraints to determine if a given field is valid
            y = int(req[0].split('-')[0])
            z = int(req[0].split('-')[1])
            a = int(req[1].split('-')[0])
            b = int(req[1].split('-')[1])
            v_con = constraint.FunctionConstraint(lambda x, y=y, z=z, a=a, b=b: y <= x <= z or a <= x <= b, ['x'])
            valid_constraints[v_con] = field

            # generate constraints for filtering out invalid tickets
            for r in req:
                r = r.split('-')
                constraints.append(constraint.FunctionConstraint(lambda x, y=int(r[0]), z=int(r[1]): x if not y <= x <= z else 0 , ['x']))
        
        # Filter out invalid tickets
        tickets = [t for t in tickets if not invalid_ticket(t, constraints)]

        # We're going to keep track of the columns we've solved
        # and remove constriants that have been individually satisified.
        # This will cause us to loop until no columns are unsatisfied
        unchecked_cols = [i for i in range(len(empty_ticket))]
        while valid_constraints:
            for i in unchecked_cols:
                # Get the respective field of all individual tickets
                # this is our puzzle input for the constraint solver
                # if the same field in every ticket satisfies the constraint,
                # it might be a good fit
                fields = [x[i] for x in tickets]
                potential_cols = []
                for c in valid_constraints.keys():
                    problem = constraint.Problem()
                    problem.addVariable('x', fields)
                    problem.addConstraint(c)
                    # This is only a good fit if every field satisifies the solution
                    if len(problem.getSolutions()) == len(fields):
                        potential_cols.append(c)
                # Ensure that only one constraint is actually satisfied.
                # if more than 1 is satisified, we can't know for sure which
                # field this column belongs to
                if len(potential_cols) == 1:
                    #print(f"Assigned column is: {valid_constraints[potential_cols[0]]}")
                    empty_ticket[i] = valid_constraints[potential_cols[0]]
                    del valid_constraints[potential_cols[0]]
                    unchecked_cols.remove(i)
        #print(empty_ticket)
        # Okay, now we need to map the empty ticket to our ticket...
        my_ticket = [int(x) for x in self.your_ticket.split('\n')[1].split(',')]
        r = 1
        for i in range(len(empty_ticket)):
            if 'departure' in empty_ticket[i]:
                r *= my_ticket[i]
        print(r)



if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.problem1()
    puzzle.problem2()