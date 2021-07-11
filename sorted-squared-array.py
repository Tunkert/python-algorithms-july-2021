# The problem: you are given an array of integers, write a function that
# contains a sorted array of those integers squared

# Modifications
# Allow user to input array length and numbers
# Not in function

# [-6, -5, 2, 3, 4] <-- input

# [4, 9, 16, 25, 36] <-- output

your_array = []
squared_array = []

print('This program will take numbers in, square them, and sort them from least to greatest. ')

while True:
    try:
        array_length = int(input('How many numbers do you want in your array? '))
        break
    except:
        print('You must enter an integer. ')

i = 0

while i < array_length:
    while True:
        try:
            next_value = int(input('What is the next number you want to enter in the array? '))
            break
        except:
            print('You must enter an integer amount. ')
    your_array.append(next_value)
    i += 1

print('Your original array is ' , your_array)

# square array and list in order

for number in your_array:
    squared_number = number * number
    squared_array.append(squared_number)

squared_array.sort()

print('Your sorted array is ' , squared_array)


