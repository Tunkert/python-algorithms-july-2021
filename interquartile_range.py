import math

class Outliers:
    def __init__(self, data_list):
        self.data_list = data_list
    
    def lower_median(self):
        lower_med_index = int(math.floor(len(data_list) / 4))
        if (math.floor(len(data_list) / 2)) % 2 == 0:
            lower_med = (data_list[lower_med_index] + data_list[lower_med_index - 1]) / 2
        else:
            lower_med = data_list[lower_med_index]
        return lower_med

    def upper_median(self):
        if (math.floor(len(data_list) / 2)) % 2 == 0:
            upper_med_index = int(math.ceil(len(data_list) * 0.75))
            upper_med = (data_list[upper_med_index] + data_list[upper_med_index - 1]) / 2
        else:
            upper_med_index = int(math.floor(len(data_list) * 0.75))
            upper_med = data_list[upper_med_index]
        return upper_med

    def interquartile_range(self):
        iq_range = self.upper_median() - self.lower_median()
        return iq_range

    def outliers(self):
        outlier = 0
        upper_outlier_value = self.upper_median() + 1.5 * self.interquartile_range()
        lower_outlier_value = self.lower_median() - 1.5 * self.interquartile_range()
        for data in self.data_list:
            if data >= upper_outlier_value or data <= lower_outlier_value:
                outlier += 1
        return outlier

# data_list = [2, 4, 4, 5, 6, 7, 8]
# data_list = [1, 3, 3, 4, 5, 6, 6, 7, 8, 8]
# data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20]

data_set = Outliers(data_list)

print(data_set.lower_median())
print(data_set.upper_median())
print(data_set.interquartile_range())
print(data_set.outliers())
        
