inte = -5001

def reverse_integer(inte):
    inte_str = str(inte)
    inte_list = [char for char in inte_str]
    rev_str = ""
    if inte_list[0] == "-":
        rev_str = "-"
        i = 1
        while i < len(inte_list):
            rev_str += inte_list[len(inte_list) - i]
            i += 1
    elif inte_list[len(inte_list) - 1] == "0":
        rev_str = ""
        i = 1
        while i < len(inte_list):
            rev_str += inte_list[len(inte_list) - i - 1]
            i += 1
    else:
        rev_str = ""
        i = 0
        while i < len(inte_list):
            rev_str += inte_list[len(inte_list) - i - 1]
            i += 1
    return rev_str

reverse_int = reverse_integer(inte)

print(reverse_int)
