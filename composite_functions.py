class CompositeFunction:
    def __init__(self, a, b, c, d, x_var):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x_var = x_var

    def make_equations(self):
        g_function = self.a * self.x_var + self.b
        h_function = self.c * g_function + self.d
        return h_function

file1 = open("composite_functions.txt", "a")
for x_var in range(2, 10):
    for a in range(2, 10):
        for b in range(2, 10):
            for c in range(2, 10):
                for d in range(2, 10):
                    new_equation = CompositeFunction(a, b, c, d,\
                                                     x_var)
                    file1.write("+++++++++++++\n")
                    file1.write(f"If g(x) = {a}x + {b} and \
h(x) = {c}x + {d}, what is h(g({x_var}))?")
                    file1.write("\n\n")
                    file1.write(f"The solution is \
 {new_equation.make_equations()}.")
                    file1.write("\n\n")
file1.close()

