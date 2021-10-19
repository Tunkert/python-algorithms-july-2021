import random

def fill_list(random_num_list):
    for x in range(-100, 100):
        random_num_list.append(x)
    return random_num_list

def in_list(choices_list, value):
    if value in choices_list:
        return True
    else:
        return False

random_num_list = []
choices_x_value_list = []
choices_y_value_list = []
choices_radius_list = []

full_random_list = fill_list(random_num_list)

circles_file = open("circles.org", "a")
circles_file_sol = open("circles-sol.org", "a")

for problem in range(1, 101):
    x_value = random.choice(full_random_list)
    y_value = random.choice(full_random_list)
    radius = random.choice(full_random_list)
    while in_list(choices_x_value_list, x_value):
        x_value = random.choice(full_random_list)
    choices_x_value_list.append(x_value)
    while in_list(choices_y_value_list, y_value):
        y_value = random.choice(full_random_list)
    choices_y_value_list.append(y_value)
    while in_list(choices_radius_list, radius) or radius == 0:
        radius = random.choice(full_random_list)
    choices_radius_list.append(radius)
    circles_file.write(f"Problem {problem}\n\n")
    circles_file.write("What is the center and radius of the circle: ")
    circles_file.write(f"(x - ({x_value}))^{2} + (y - ({y_value}))^{2} = {radius ** 2}?\n\n")
    circles_file.write("---\n\n")
    circles_file_sol.write(f"Problem {problem}\n\n")
    circles_file_sol.write(f"Solution: center ({x_value}, {y_value}), radius = {abs(radius)}\n\n")
    circles_file_sol.write("---\n\n")

circles_file.close()
circles_file_sol.close()
