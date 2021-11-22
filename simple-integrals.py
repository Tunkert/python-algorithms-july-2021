from math import exp
import random

class SimpleIntegral:
    def __init__(self, lower_range, upper_range, exponent):
        self.lower_range = lower_range
        self.upper_range = upper_range
        self.exponent = exponent

    def value_integral(self):
        upper_value = ((self.upper_range) ** (self.exponent + 1)) / (self.exponent + 1)
        lower_value = ((self.lower_range) ** (self.exponent + 1)) / (self.exponent + 1)
        value = upper_value - lower_value
        return value

random_num_list = []
exponent_list = [2, 3, 4, 5, 6, 7, 8]

for x in range(0, 51):
    random_num_list.append(x)

simple_integral_file = open("simple-integral.tex", "a")
simple_integral_spanish_file = open("simple-integral-spanish.tex", "a")
simple_integral_sol_file = open("simple-integral-sol.tex", "a")
simple_integral_sol_spanish_file = open("simple-integral-sol-spanish.tex", "a")

simple_integral_file.write(r"\documentclass{article}")
simple_integral_spanish_file.write(r"\documentclass{article}")
simple_integral_sol_file.write(r"\documentclass{article}")
simple_integral_sol_spanish_file.write(r"\documentclass{article}")

simple_integral_file.write("\n\n")
simple_integral_spanish_file.write("\n\n")
simple_integral_sol_file.write("\n\n")
simple_integral_sol_spanish_file.write("\n\n")

simple_integral_file.write(r"\begin{document}")
simple_integral_spanish_file.write(r"\begin{document}")
simple_integral_sol_file.write(r"\begin{document}")
simple_integral_sol_spanish_file.write(r"\begin{document}")

simple_integral_file.write("\n\n")
simple_integral_spanish_file.write("\n\n")
simple_integral_sol_file.write("\n\n")
simple_integral_sol_spanish_file.write("\n\n")

for problem in range(1, 101):
    lower_range = random.choice(random_num_list)
    upper_range = random.choice(random_num_list)

    while lower_range > upper_range or lower_range == upper_range:
        lower_range = random.choice(random_num_list)
        upper_range = random.choice(random_num_list)
        
    exponent = random.choice(exponent_list)
    new_problem = SimpleIntegral(lower_range, upper_range, exponent)
    simple_integral_file.write(f"Problem {problem}\n\n")
    simple_integral_spanish_file.write(f"Problema {problem}\n\n")
    simple_integral_sol_file.write(f"Problem {problem}\n\n")
    simple_integral_sol_spanish_file.write(f"Problema {problem}\n\n")
    simple_integral_file.write(r"\[ \int_{")
    simple_integral_file.write(f"{lower_range}")
    simple_integral_file.write(r"}^{")
    simple_integral_file.write(f"{upper_range}")
    simple_integral_file.write(r"} x^")
    simple_integral_file.write(f"{exponent}")
    simple_integral_file.write(r"\,dx \]")
    simple_integral_file.write("\n\n")
    simple_integral_spanish_file.write(r"\[ \int_{")
    simple_integral_spanish_file.write(f"{lower_range}")
    simple_integral_spanish_file.write(r"}^{")
    simple_integral_spanish_file.write(f"{upper_range}")
    simple_integral_spanish_file.write(r"} x^")
    simple_integral_spanish_file.write(f"{exponent}")
    simple_integral_spanish_file.write(r"\,dx \]")
    simple_integral_spanish_file.write("\n\n")
    simple_integral_sol_file.write(f"Solution: {new_problem.value_integral()}\n\n")
    simple_integral_sol_spanish_file.write(f"Solucion: {new_problem.value_integral()}\n\n")

simple_integral_file.write(r"\end{document}")
simple_integral_spanish_file.write(r"\end{document}")
simple_integral_sol_file.write(r"\end{document}")
simple_integral_sol_spanish_file.write(r"\end{document}")

simple_integral_file.close()
simple_integral_spanish_file.close()
simple_integral_sol_file.close()
simple_integral_sol_spanish_file.close()
