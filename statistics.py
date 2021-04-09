import math
import data

def sum(values):
    sum_values = 0
    for value in values:
        sum_values += value
    return sum_values

def mean(values):
    return sum(values)/len(values)
def median(values):
    values.sort()
    if len(values) % 2 == 0:
        x1 = values[math.ceil(len(values)/2) - 1]
        x2 = values[math.ceil(len(values)/2)]
        return (x1 + x2)/2
    return values[math.ceil(len(values)/2) - 1]

def population_statistics(feature_description, data1, treatment, target, threshold, is_above,
statistic_functions):
    print(feature_description)
    dic = {}
    for key in list(data1.keys()):
        dic.setdefault(key, [])
    if is_above:
        for row, value in enumerate(data1[treatment]):
            if value > threshold:
                for key in list(data.keys()):
                    dic[key].append(data1[key][row])
    else:
        for row, value in enumerate(data1[treatment]):
            if value <= threshold:
                for key in list(data1.keys()):
                    dic[key].append(data1[key][row])
    data.print_details(dic, [target], statistic_functions)