import math

while True:
    try:
        a = int(input("What is the value of a? "))
        break
    except:
        print("You must enter an integer.")

while True:
    try:
        b = int(input("What is the value of b? "))
        break
    except:
        print("You must enter an integer.")

while True:
    try:
        c = int(input("What is the value of c? "))
        break
    except:
        print("You must enter an integer.")

def quadratic_formula(a, b, c):
    if b * b - 4 * a * c >= 0:
        sol_1 = ((-1 * b) + math.pow(b * b - 4 * a * c, 0.5)) / (2 * a)
        sol_2 = ((-1 * b) - math.pow(b * b - 4 * a * c, 0.5)) / (2 * a)
        ans_str = f"The solutions are x = {sol_1} and x = {sol_2}."
    else:
        ans_str = "There are no real solutions to this equation."
    return ans_str

solution = quadratic_formula(a, b, c)

print(solution)
