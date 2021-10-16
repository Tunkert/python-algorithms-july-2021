import random

class PoolPerimeter:
    def __init__(self, additional_value):
        self.additional_value = additional_value

    def perimeter(self):
        perimeter_addition = self.additional_value * 2
        return perimeter_addition

random_num_list = []
for x in range(1, 201):
    random_num_list.append(x)

pool_perimeter_file = open("pool-perimeter-file.org", "a")
pool_perimeter_file_sol = open("pool-perimeter-file-sol.org", "a")

for problem in range(1, 26):
    additional_value = random.choice(random_num_list)
    new_problem = PoolPerimeter(additional_value)
    pool_perimeter_file.write(f"*Problem {problem}* \n\n")
    pool_perimeter_file.write(f"If the width of a pool is \
x yards, and the length of the pool is {additional_value} \
yard(s) more than the width, what is the perimeter of the \
pool?\n\n")
    pool_perimeter_file.write("---\n\n")
    pool_perimeter_file_sol.write(f"*Problem {problem}* \n\n")
    pool_perimeter_file_sol.write(f"Solution: 4x + \
{new_problem.perimeter()} yards.\n\n")
    pool_perimeter_file_sol.write("---\n\n")

pool_perimeter_file.close()
pool_perimeter_file_sol.close()
