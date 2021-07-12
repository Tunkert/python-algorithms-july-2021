s = "babad"
# output must be "bab" or "aba"

def cycle(s):
    x = [char for char in s]
    y = []
    i = 0
    while i < len(x):
        if x[i] == x[-1 * i - 1]:
            y.append(x[i])
        i += 1
    if y == []:
        y.append(x[0])
    return string_to_list(y)

def string_to_list(y):
    str = ""
    for letter in y:
        str += letter
    return str


pal = cycle(s)

print(pal)
