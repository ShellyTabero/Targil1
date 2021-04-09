import sys
import pandas
import data
import statistics


def q1(dic):
    print("Question1:")
    feature = ["hum", "t1", "cnt"]
    categories = ["season", "is_holiday"]
    names = ["Summer:","Holiday:"]
    methods = [statistics.sum, statistics.mean, statistics.median]
    for index, category in enumerate(categories):
        print(names[index])
        data1, data2 = data.filter_by_feature(dic, category, {1})
        data.print_details(data1, feature, methods)
    print("All:")
    data.print_details(dic, feature, methods)

def q2(dic):
    print("Question 2:")
    dic_winter, dic_not_winter = data.filter_by_feature(dic, "season", {2})
    dic_is_holiday, dic_not_holiday = data.filter_by_feature(dic_winter, "is_holiday", {0})
    print("is", dic_not_holiday)
    methods = [statistics.mean, statistics.median]
    print("If t1<=13.0, then:")
    statistics.population_statistics("Winter holiday records:", dic_is_holiday, "t1", "cnt", 13.0, False, methods)
    statistics.population_statistics("Winter weekday records:", dic_not_holiday, "t1", "cnt", 13.0, False, methods)
    #print("If t1>13.0, then:")
    #statistics.population_statistics("Winter holiday records:", dic_is_holiday, "t1", "cnt", 13.0, True, methods)
    #statistics.population_statistics("Winter weekday records:", dic_not_holiday, "t1", "cnt", 13.0, True, methods)

def main(argv):
    dic = data.load_data(argv[1], argv[2])
    q1(dic)
    q2(dic)

if __name__ == '__main__':
    main(sys.argv)