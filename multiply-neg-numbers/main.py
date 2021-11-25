import os
import sys
import random

sys.path.append(".")

from lists import NumList
from products import Multiply

mult_file = open("mult.md", "a")
mult_sol_file = open("mult-sol.md", "a")
mult_span_file = open("mult-span.md", "a")

rand_list = NumList.random_list()

for problem in range(1, 101):
    constant_one = random.choice(rand_list)
    constant_two = random.choice(rand_list)
    
    sign_choice = NumList
    the_sign = random.choice(sign_choice.sign_list())
    the_sign_2 = random.choice(sign_choice.sign_list())
    if the_sign == 0:
        constant_one = constant_one * -1
    if the_sign_2 == 0:
        constant_two == constant_two * -1
    
    new_problem = Multiply(constant_one, constant_two)
    
    mult_file.write(f"## Problem {problem}\n\n")
    mult_sol_file.write(f"## Problem {problem}\n\n")
    mult_span_file.write(f"## Problema {problem}\n\n")
    
    mult_file.write(f"What is {constant_one} x {constant_two}?\n\n")
    mult_span_file.write(f"Que es {constant_one} x {constant_two}\n\n")
    mult_sol_file.write(f"Solution (solucion): {new_problem.the_product()}\n\n")
    
    mult_file.write("---\n\n")
    mult_span_file.write("---\n\n")
    mult_sol_file.write("---\n\n")
    
mult_file.close()
mult_sol_file.close()
mult_span_file.close()

    
