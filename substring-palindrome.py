str = "sublevel"

def pal_sub(str):
    str_list = [char for char in str]
    i = 1
    center = 0
    pal = ""
    max_length = 0
    start = 0
    while i < len(str_list) - 1:
        n = 1
        if str_list[i - 1] == str_list[i + 1]:
            while n < len(str_list) - (i):
                if str_list[i - n] == str_list[i + n]:
                    max_length = 2 * n
                    start = i - n
                n += 1
        i += 1
    it = 0
    if max_length == 0:
        while it < len(str_list):
            if str_list[it - 1] == str_list[it]:
                if len(str_list) == 1:
                    max_length = 0
                    start = 0
                else:
                    max_length = 1
                    start = it - 1
            it += 1
    x = 0
    while x <= max_length:
        pal += str_list[start + x]
        x += 1
    return pal

list = pal_sub(str)

print(list)
    
