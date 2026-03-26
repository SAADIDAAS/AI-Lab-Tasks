from ortools.sat.python import cp_model

class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, queens):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__queens = queens
        self.__solution_count = 0

    def on_solution_callback(self):
        if self.__solution_count == 0:
            print("\nTask 7: 4-Queens Solution")
            for i in range(len(self.__queens)):
                for j in range(len(self.__queens)):
                    if self.value(self.__queens[j]) == i:
                        print("Q", end=" ")
                    else:
                        print("_", end=" ")
                print()
        self.__solution_count += 1

def solve_n_queens(board_size=4):
    model = cp_model.CpModel()
    queens = [model.new_int_var(0, board_size - 1, f'x_{i}') for i in range(board_size)]

    model.add_all_different(queens)
    model.add_all_different([queens[i] + i for i in range(board_size)])
    model.add_all_different([queens[i] - i for i in range(board_size)])

    solver = cp_model.CpSolver()
    solution_printer = NQueenSolutionPrinter(queens)
    solver.parameters.enumerate_all_solutions = True
    solver.solve(model, solution_printer)

solve_n_queens()
