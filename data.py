import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    for key in list(data.keys()):
        if key not in features:
            data.pop(key)
    return data


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    all_features = list(data.keys())
    for key in all_features:
        data1.setdefault(key, [])
        data2.setdefault(key, [])
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
        results = []
        print(category, end=": ")
        for method in statistic_functions:
            results.append(str(method(lst)))
        print(", ".join(results))
