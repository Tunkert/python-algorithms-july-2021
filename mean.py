def find_mean(data_list):
    sum = 0
    i = 0
    while i < len(data_list):
        sum += data_list[i]
        i += 1
    mean = sum / len(data_list)
    return mean

data_list = [1, 2, 3, 4, 5, 6, 7, 101, 2]
average = find_mean(data_list)

print(average)

