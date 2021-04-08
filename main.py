import sys
import pandas
import data
import statistics


def q1(dic):
    feature = ["hum", "t1", "cnt"]
    categories=["season", "is_holiday"]
    names=["Summer:","Holiday:"]
    methods = [statistics.sum, statistics.mean, statistics.median]
    for index, category in enumerate(categories):
        print(names[index])
        data1,data2 = data.filter_by_feature(dic, category, {1})
        data.print_details(data1, feature, methods)
    print("All:")
    data.print_details(dic, feature, methods)

def q2(dic):
    print("Question 2:")
    data1, data2 = data.filter_by_feature(dic,"is_holiday", {1})
    methods = [statistics.mean, statistics.median]
    print("If t1<=13.0, then:")
    statistics.population_statistics("Winter holiday records:", data1, "t1", "cnt", 13.0, False, methods)
    statistics.population_statistics("Winter weekday records:", data2, "t1", "cnt", 13.0, False, methods)
    print("If t1>13.0, then:")
    statistics.population_statistics("Winter holiday records:", data1, "t1", "cnt", 13.0, True, methods)
    statistics.population_statistics("Winter weekday records:", data2, "t1", "cnt", 13.0, True, methods)

def main(argv):
    dic = data.load_data(argv[1], argv[2])
    q1(dic)
    q2(dic)

if __name__ == '__main__':
    main(sys.argv)