import random

class Quadratic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def coefficient_one(self):
        coefficient_1 = 1
        return coefficient_1

    def coefficient_two(self):
        coefficient_2 = self.a + self.b
        return coefficient_2

    def constant_one(self):
        constant_1 = self.a * self.b
        return constant_1
    
file1 = open("factoring.md", "a")
for x in range(0, 9):
    random_list = [2, 3, 4, 5, 6, 7, 8, 9]
    a = random.choice(random_list)
    b = random.choice(random_list)
    new_quadratic = Quadratic(a, b)
    file1.write("<div class='col-md-4'>\n")
    file1.write(f"<h3>Problem {x + 1}</h3>\n")
    file1.write("<p>Factor the following:\n <br>\n")
    file1.write(f"{new_quadratic.coefficient_one()}x<sup>2</sup> + ")
    file1.write(f"{new_quadratic.coefficient_two()}x + ")
    file1.write(f"{new_quadratic.constant_one()}.</p>\n <br><br><br><br><br>\n")
    file1.write("</div>\n")
file1.close()
