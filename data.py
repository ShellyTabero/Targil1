import pandas
def load_data(path,features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return data

def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    all_features = list(data.keys())
    for all_features in data:
        data1.setdefault(all_features, [])
        data2.setdefault(all_features, [])
    #data1 = {"cnt":[], "season":[], "is_holiday":[],"hum":[],"t1":[]}
    #data2 = {"cnt":[], "season":[], "is_holiday":[],"hum":[],"t1":[]}
    lst = data[feature]
    for index, value in enumerate(lst):
        if value in values:
            for category in all_features:
                data1[category].append(data[category][index])
        else:
            for category in all_features:
                data2[category].append(data[category][index])
    return data1, data2

def print_details(data, features, statistic_functions):
    for category in features:
        lst = data[category]
        print(category, end=": ")
        for method in statistic_functions:
            print("{}, ".format(method(lst)), end=" ")
        print("\n")
        """sum = statistic_functions[0](lst)
        mean = statistic_functions[1](lst)
        median = statistic_functions[2](lst)
        print("{}: {}, {}, {}".format(category, sum, mean, median))"""