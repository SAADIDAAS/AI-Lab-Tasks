from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._variables = variables
        self._solution_count = 0

    def on_solution_callback(self):
        self._solution_count += 1
        for v in self._variables:
            print(f"{v}={self.value(v)}", end="  ")
        print()

def solve_basic_csp():
    model = cp_model.CpModel()
    A = model.new_int_var(0, 3, 'A')
    B = model.new_int_var(0, 3, 'B')
    C = model.new_int_var(0, 3, 'C')

    model.add(A != B)
    model.add(B != C)
    model.add(A + B <= 4)

    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True
    solution_printer = VarArraySolutionPrinter([A, B, C])
    
    print("Task 4 & 5: CSP Solutions")
    status = solver.solve(model, solution_printer)
    print(f"Total solutions found: {solution_printer._solution_count}")

solve_basic_csp()
