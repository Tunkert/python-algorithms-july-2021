# I   1
# V   5
# X   10
# L   50
# C   100
# D   500
# M   1000

s = "III"
# s = "IV"
# s = "IX"
# s = "LVIII"
# s = "MCMXCIV"
# s = "III"

def roman_to_int(s):
    s_list = [char for char in s]
    i = 0
    sum = 0
    while len(s_list) > 1 and i < len(s_list) - 1:
        if s_list[i] == "I" and s_list[i + 1] == "V" or s_list[i] == "I" and s_list[i + 1] == "X":
            sum -= 1
        elif s_list[i] == "I":
            sum += 1
        if s_list[i] == "X" and s_list[i + 1] == "L" or s_list[i] == "X" and s_list[i + 1] == "C":
            sum -= 10
        elif s_list[i] == "X":
            sum += 10
        if (s_list[i] == "C" and s_list[i + 1] == "D") or (s_list[i] == "C" and s_list[i + 1] == "M"):
            sum -= 100
        elif s_list[i] == "C":
            sum += 100
        if s_list[i] == "V":
            sum += 5
        if s_list[i] == "L":
            sum += 50
        if s_list[i] == "D":
            sum += 500
        if s_list[i] == "M":
            sum += 1000
        i += 1   
    if s_list[i] == "I":
        sum += 1
    if s_list[i] == "V":
        sum += 5
    if s_list[i] == "X":
        sum += 10
    if s_list[i] == "L":
        sum += 50
    if s_list[i] == "C":
        sum += 100
    if s_list[i] == "D":
        sum += 500
    if s_list[i] == "M":
        sum += 1000
    return sum

solution = roman_to_int(s)

print(f"The solution is {solution}.")