x = 101

def isPalindrome(x):
    y = str(x)
    x_list = [num for num in y]
    a = True
    i = 0
    while i < len(x_list):
        if x_list[i] != x_list[-1 * i - 1]:
            a = False
        i += 1
    return a

print(isPalindrome(x))
