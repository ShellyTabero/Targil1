import math

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

def population_statistics(feature_description, data, treatment, target, threshold, is_above,
statistic_functions):

    lst = []
    if is_above:
        for index, value in enumerate(data[treatment]):
            if value > threshold:
                lst.append(data[target][index])
    else:
        for index, value in enumerate(data[treatment]):
            if value <= threshold:
                lst.append(data[target][index])
    print("{}: {}, {}".format(target, statistic_functions[1](lst), statistic_functions[2](lst)))