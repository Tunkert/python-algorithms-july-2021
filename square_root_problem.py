class SquareRootEq:
    def __init__(self, c1, c2, c3, c4, c5):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5

    def equal_sides(self):
        solutions_list = []
        for x in range(0, 101):
            left_side = (self.c1 * x + self.c2) ** (0.5) + self.c3
            right_side = self.c4 * x + self.c5
            if left_side == right_side:
                solutions_list.append(x)
        return solutions_list

file1 = open("square_root_equations.txt", "a")
for c1 in range(2, 11):
    for c2 in range(2, 11):
        for c3 in range(2, 11):
            for c4 in range(2, 11):
                for c5 in range(2, 11):
                    the_equation = SquareRootEq(c1, c2, c3, c4, c5)
                    equation_solution = the_equation.equal_sides()

                    if equation_solution != None:
                        for solution in equation_solution:
                            if solution != 1 and solution != 0:
                                file1.write("==========\n")
                                file1.write(str(solution) + "a\n")
                                file1.write(f"c1 = {c1}, c2 = {c2}, c3 = {c3}, c4 = {c4}, c5 = {c5}")
                                file1.write("\n\n")
                    else:
                        print("There are no solutions to this equation")
file1.close()
        
