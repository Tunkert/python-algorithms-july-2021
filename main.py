import sys
import os
import random

sys.path.append(".")

from fraction_to_decimal import FractionToDecimal
from random_list import RandomList

new_list = RandomList

frac_file = open("frac.tex", "a")
frac_span_file = open("frac-span.tex", "a")
frac_sol_file = open("frac-sol.tex", "a")
frac_span_sol_file = open("frac-span-sol.tex", "a")

frac_file.write(r"\documentclass{article}")
frac_span_file.write(r"\documentclass{article}")
frac_sol_file.write(r"\documentclass{article}")
frac_span_sol_file.write(r"\documentclass{article}")

frac_file.write("\n\n")
frac_span_file.write("\n\n")
frac_sol_file.write("\n\n")
frac_span_sol_file.write("\n\n")

frac_file.write(r"\begin{document}")
frac_span_file.write(r"\begin{document}")
frac_sol_file.write(r"\begin{document}")
frac_span_sol_file.write(r"\begin{document}")

frac_file.write("\n\n")
frac_span_file.write("\n\n")
frac_sol_file.write("\n\n")
frac_span_sol_file.write("\n\n")

frac_file.write("Convert the following fractions to decimals, round to \
two decimal places if necessary.\n\n")
frac_span_file.write("Convierta las siguientes fracciones a decimales, \
redondee a dos lugares decimales si es necesario")

for problem in range(1, 101):
    numerator = random.choice(new_list.random_list())
    denominator = random.choice(new_list.random_list())

    new_problem = FractionToDecimal(numerator, denominator)

    frac_file.write(f"Problem {problem}\n\n")
    frac_span_file.write(f"Problema {problem}\n\n")
    frac_sol_file.write(f"Problem {problem}\n\n")
    frac_span_sol_file.write(f"Problema {problem}\n\n")

    frac_file.write(r"\[\frac{")
    frac_span_file.write(r"\[\frac{")

    frac_file.write(f"{numerator}")
    frac_span_file.write(f"{numerator}")

    frac_file.write(r"}{")
    frac_span_file.write(r"}{")

    frac_file.write(f"{denominator}")
    frac_span_file.write(f"{denominator}")

    frac_file.write(r"}\]")
    frac_span_file.write(r"}\]")

    frac_file.write("\n\n")
    frac_span_file.write("\n\n")

    frac_sol_file.write(f"Solution: {round(new_problem.decimal_value(), 2)}\n\n")
    frac_sol_file.write(f"Solucion: {round(new_problem.decimal_value(), 2)}\n\n")

frac_file.write(r"\end{document}")
frac_span_file.write(r"\end{document}")
frac_sol_file.write(r"\end{document}")
frac_span_sol_file.write(r"\end{document}")
