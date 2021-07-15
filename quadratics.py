import math

a = 4
b = 3
c = 8

def quadratic_formula(a, b, c):
    if b * b - 4 * a * c >= 0:
        sol_1 = ((-1 * b) + math.pow(b * b - 4 * a * c, 0.5)) / (2 * a)
        sol_2 = ((-1 * b) - math.pow(b * b - 4 * a * c, 0.5)) / (2 * a)
        ans_str = f"The solutions are x = {sol_1} and x = {sol_2}."
    else:
        ans_str = "There are no real solutions to this equation."
    return ans_str

solution = quadratic_formula(1, -7, 10)

print(solution)
