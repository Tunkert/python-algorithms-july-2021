import random

class CompositeProblem:
  def __init__(self, real_1, imag_1, real_2, imag_2):
    self.real_1 = real_1
    self.imag_1 = imag_1
    self.real_2 = real_2
    self.imag_2 = imag_2

  def find_sum_real(self):
    sum_real = self.real_1 + self.real_2
    return sum_real

  def find_sum_imag(self):
    sum_imag = self.imag_1 + self.imag_2
    return sum_imag

  def find_diff_real(self):
    diff_real = self.real_1 - self.real_2
    return diff_real

  def find_diff_imag(self):
    diff_imag = self.imag_1 - self.imag_2
    return diff_imag

random_num_list = []
operation_choice_list = [0, 1]

for x in range(-100, 101):
  random_num_list.append(x)

complex_addition_problem_file = open("complex-addition.md", "a")
complex_addition_problem_file_sol = open("complex-addition-sol.md", "a")

for problem in range(1, 101):
  real_1 = random.choice(random_num_list)
  imag_1 = random.choice(random_num_list)
  real_2 = random.choice(random_num_list)
  imag_2 = random.choice(random_num_list)
  operation_choice = random.choice(operation_choice_list)

  new_problem = CompositeProblem(real_1, imag_1, real_2, imag_2)
  complex_addition_problem_file.write("## English version\n\n")
  complex_addition_problem_file.write(f"### Problem {problem}\n\n")
  if operation_choice == 0:
    complex_addition_problem_file.write(f"What is the sum of \
({real_1} + {imag_1}i) + ({real_2} + {imag_2}i)?\n\n")
  else:
    complex_addition_problem_file.write(f"What is the difference of \
({real_1} + {imag_1}i) - ({real_2} + {imag_2}i)?\n\n")
  complex_addition_problem_file.write("---\n\n")
  complex_addition_problem_file.write("## Versión en español\n\n")
  complex_addition_problem_file.write(f"### Problema {problem}\n\n")
  if operation_choice == 1:
    complex_addition_problem_file.write(f"Cual es la diferencia de \
({real_1} + {imag_1}i) - ({real_2} + {imag_2}i)?\n\n")
  else:
    complex_addition_problem_file.write(f"Cuál es la suma de \
({real_1} + {imag_1}i) + ({real_2} + {imag_2}i)?\n\n")
  complex_addition_problem_file.write("---\n\n")

  # solutions
  complex_addition_problem_file_sol.write(f"### Problem (problema) {problem}\n\n")
  if operation_choice == 0:
    complex_addition_problem_file_sol.write(f"Solution (solución): \
{new_problem.find_sum_real()} + {new_problem.find_sum_imag()}i\n\n")
  else:
    complex_addition_problem_file_sol.write(f"Solution (solución): \
{new_problem.find_diff_real()} + {new_problem.find_diff_imag()}i\n\n")
  complex_addition_problem_file_sol.write("---\n\n")

complex_addition_problem_file.close()
complex_addition_problem_file_sol.close()
    


