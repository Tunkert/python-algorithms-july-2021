import random

class Pythagorean:
    def __init__(self, a, b, choice):
        self.a = a
        self.b = b
        self.choice = choice

    def pick_type(self):
        if self.choice == 0:
            type_hyp = True
        else:
            type_hyp = False
        return type_hyp

    def find_hypotenuse(self):
        hypotenuse = (self.a ** 2 + self.b **2) ** (0.5)
        return hypotenuse

random_num_list = []
choice_list = [0, 1]

for x in range(1, 51):
    random_num_list.append(x)

pythagorean_file = open("pythagorean_file.md", "a")
pythagorean_file_sol = open("pythagorean_file_sol.md", "a")

for problem in range(1, 101):
    a = random.choice(random_num_list)
    b = random.choice(random_num_list)
    choice = random.choice(choice_list)
    new_problem = Pythagorean(a, b, choice)
    pythagorean_file.write(f"## Problem {problem}\n\n")
    if new_problem.pick_type():
        pythagorean_file.write(f"If the legs of a right triangle \
are lengths of {a} unit(s) and {b} unit(s) respectively, what is the \
length of the hypotenuse, c? (Round to two decimal places if necessary.)\n\n")
    else:
        pythagorean_file.write(f"If the hypotenuse, c, of a right triange \
has a length of {round(new_problem.find_hypotenuse(), 2)} unit(s) and the length \
of one leg, a, is {a} unit(s), what is the length of the other side, b, of \
the right triangle? (Round to two decimal places if necessary)\n\n")
    pythagorean_file.write("![right triangle](abc-triangle.png)\n\n")
    pythagorean_file.write("---\n\n")
    pythagorean_file_sol.write(f"## Problem {problem}\n\n")
    if new_problem.pick_type():
        pythagorean_file_sol.write(f"Solution: {round(new_problem.find_hypotenuse(), 2)} unit(s)\n\n")
    else:
        pythagorean_file_sol.write(f"Solution: {b} unit(s)\n\n")
    pythagorean_file_sol.write("---\n\n")

pythagorean_file.close()
pythagorean_file_sol.close()
