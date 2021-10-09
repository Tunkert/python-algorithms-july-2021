import random

class FactorableQuadratic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def coefficient_one(self):
        c_1 = 1
        return c_1

    def coefficient_two(self):
        c_2 = self.a + self.b
        return c_2

    def constant_one(self):
        const_1 = self.a * self.b
        return const_1

class UnFactorableQuadratic:
    def __init__(self, c, d):
        self.c = c
        self.d = d

    def factors_list(self):
        factors_list_products = []
        for x in range(1, self.d):
            if self.d % x == 0:
                factors_list_products.append(x)
        return factors_list_products

    def factors_sums(self):
        sums_list = []
        factors = self.factors_list()
        for factor in factors:
            if self.d % factor == 0:
                sums_list.append(self.d / factor + factor)
        return sums_list

    def factorable_boolean(self):
        factorable = False
        sums = self.factors_sums()
        for sum in sums:
            if sum == self.c:
                factorable = True
        return factorable

file1 = open("quadratics.org", "a")
file2 = open("solutions.org", "a")
file1.write("* Quadratics Worksheet\n\n")
file2.write("* Solutions \n\n")

constants_list = []
random_unfactorable = [2, 3, 4]

for number in range(0, 20):
    constants_list.append(1 + number)

for problem in range(0, 100):
    file1.write(f"** Problem {problem + 1}\n")
    non_factorable_index = random.choice(random_unfactorable)
    if problem == non_factorable_index:
        c = random.choice(constants_list)
        d = random.choice(constants_list)
        new_equation = UnFactorableQuadratic(c, d)
        while new_equation.factorable_boolean():
            c = random.choice(constants_list)
            d = random.choice(constants_list)
            new_equation = unFactorableQuadratic(c, d)
        file2.write(f"** Problem {problem + 1} Solution: not factorable\n\n")
        file1.write("Factor the following quadratic: ")
        file1.write(f"x^2 + {c}x + {d}\n")
    else:
        a = random.choice(constants_list)
        b = random.choice(constants_list)
        new_equation = FactorableQuadratic(a, b)
        file1.write("Factor the following quadratic:")
        file1.write(f"{new_equation.coefficient_one()}x^2\
 + {new_equation.coefficient_two()}x + {new_equation.constant_one()}")
        file2.write(f"** Problem {problem + 1} Solution: (x + {a})(x + {b})\n\n")
        file1.write("\n")
        
file1.close()
file2.close()

            

    
