import math

data_set = [1, 2, 3, 4, 5]

def std_dev(data_set):
    sum = 0
    i = 0
    while i < len(data_set):
        sum += data_set[i]
        i += 1
    mean = sum / len(data_set)
    x = 0
    variance_sum = 0
    while x < len(data_set):
        variance_sum += math.pow((data_set[x] - mean), 2)
        x += 1
    variance = variance_sum / (len(data_set) - 1)
    stand_dev = math.pow(variance, 0.5)
    return stand_dev

standard_deviation = std_dev(data_set)

print(standard_deviation)
    
