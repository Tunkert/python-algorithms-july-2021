import math

def area_between_curves(curve_one_power, curve_two_power, x_value_1, x_value_2):
    area_one = math.pow(x_value_2, curve_one_power + 1) / (curve_one_power + 1) - math.pow(x_value_1, curve_one_power + 1) / (curve_one_power + 1)
    area_two= math.pow(x_value_2, curve_two_power + 1) / (curve_two_power + 1) - math.pow(x_value_1, curve_two_power + 1) / (curve_two_power + 1)
    area_between = area_two - area_one

    return area_between

curve_one_power = int(input("What is the power of curve one? "))
curve_two_power = int(input("What is the power of curve two? "))
x_value_1 = int(input("What is the lesser value of x? "))
x_value_2 = int(input("What is the greater value of x? "))

solution = area_between_curves(curve_one_power, curve_two_power, x_value_1, x_value_2)

print("The area between the two curves is " + str(solution) + " square units.\n")
