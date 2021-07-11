# You are given two linked lists
# They represent two non-negative numbers
# They are in reverse order
# return sum as linked list in reverse order

# Example 1 
# Input l1 = [4, 3, 1] l2 = [8, 7, 1]
# Output [2, 1, 3] because 134 + 178 = 312

# Example 2
# Input l1 = [8, 7, 7, 9, 9, 0] l2 = [9. 9. 6]
# Output [7, 4, 4, 0, 0, 1] because 99778 + 669 = 100447

# create two empty lists
list_1 = []
list_2 = []

# let user input number of integers in first list

while True:
    try:
        list_1_length = int(input('How many numbers do you want in the first list? '))
        break
    except:
        print('You must enter an integer for the number of items. ')

# let user input integers for array

i = 0

while i < list_1_length:
    while True:
        try:
            next_number_1 = int(input('What is the next number in your array? '))
            break
        except:
            print('You must enter an integer. ')
    list_1.append(next_number_1)
    i += 1

# let user input number of integers in second list

while True:
    try:
        list_2_length = int(input('How many numbers do you want in the second list? '))
        break
    except:
        print('You must enter an integer for the number of items. ')

# let user input integers for array

x = 0

while x < list_2_length:
    while True:
        try:
            next_number_2 = int(input('What is the next number in your array? '))
            break
        except:
            print('You must enter an integer. ')
    list_2.append(next_number_2)
    x += 1

# print both list

print(f'Your first list is {list_1}.')
print(f'Your second list is {list_2}.')

# reverse list 1 

list_1.reverse()

# reverse list 2

list_2.reverse()

# print both list

print(f'Your first list reversed is {list_1}.')
print(f'Your second list reversed is {list_2}.')

# convert reversed list 1 to an integer

number_1_list = [str(number) for number in list_1]
list_1_str = "".join(number_1_list)
integer_1 = int(list_1_str)

# print first integer formed

print(f'Your first integer is {integer_1}.')

# convert reversed list 2 to an integer

number_2_list = [str(number_2) for number_2 in list_2]
list_2_str = "".join(number_2_list)
integer_2 = int(list_2_str)

# print second integer formed

print(f'Your second integer is {integer_2}.')

# add the two integers

sum = integer_1 + integer_2

# print sum

print(f'Your sum of the two integers is {sum}')

# convert sum to str

sum_str = str(sum)

# split string into list

sum_str_list = [num for num in sum_str]

# print list

print(sum_str_list)

# reverse list

sum_str_list.reverse()

# print reversed list

print(sum_str_list)

output_list = []

# change list to integers

for y in sum_str_list:
    int_num = int(y)
    output_list.append(int_num)

# print output

print(f'The output is {output_list}.')







