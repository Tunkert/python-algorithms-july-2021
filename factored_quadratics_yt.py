import math
import random

class FactoredQuadratic:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def coefficient_one(self):
        c_1 = self.a * self.c
        return c_1

    def coefficient_two(self):
        c_2 = self.a * self.d + self.b * self.c
        return c_2

    def constant_one(self):
        constant_1 = self.b * self.d
        return constant_1

file1 = open("development.html", "a")
file1.write("<div class='container'>")
file1.write("<div class='row'>")
for x in range(1, 11):
    list_of_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = random.choice(list_of_choices) 
    b = random.choice(list_of_choices) 
    c = random.choice(list_of_choices) 
    d = random.choice(list_of_choices) 
    new_equation = FactoredQuadratic(a, b, c, d) 
    file1.write("<div class='col-12 col-md-4 text-center'")
    file1.write(f"<h3>Problem #{x}</h3>")
    file1.write("<p>Factor the following quadratic:</p>")
    file1.write(f"<p>{new_equation.coefficient_one()}x<sup>2</sup> \
+ {new_equation.coefficient_two()}x + {new_equation.constant_one()}.</p>")
    file1.write("</div>")
file1.write("</div>")
file1.write("</div>")
file1.close()
