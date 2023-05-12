# Knowledge Sources
class SourceA:
    def contribute_knowledge(self, blackboard):
        data = "Knowledge from Source A"
        blackboard.add_data(data)

class SourceB:
    def contribute_knowledge(self, blackboard):
        data = "Knowledge from Source B"
        blackboard.add_data(data)

# Blackboard
class Blackboard:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

# Problem Solver
class ProblemSolver:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def solve_problem(self):
        data = self.blackboard.get_data()
        # Perform problem-solving using the available knowledge
        for item in data:
            print("Processing data:", item)

# Main program
if __name__ == '__main__':
    # Create instances of the knowledge sources and the blackboard
    source_a = SourceA()
    source_b = SourceB()
    blackboard = Blackboard()

    # Contribute knowledge to the blackboard
    source_a.contribute_knowledge(blackboard)
    source_b.contribute_knowledge(blackboard)

    # Solve the problem using the knowledge on the blackboard
    problem_solver = ProblemSolver(blackboard)
    problem_solver.solve_problem()
