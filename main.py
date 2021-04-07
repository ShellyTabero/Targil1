import sys
import pandas
import data
import statistics

def main (argv):
    pass
if __name__ == '__main__':
    main(sys.argv)
    dic = data.load_data('london.csv', ['cnt', 'season', 'is_holiday', 'hum', 't1'])
    data.filter_by_feature(dic, "season", {1,2})
    feat = ["season", "is_weekend"]
    stat = [statistics.sum, statistics.mean, statistics.median]
    data.print_details(dic, feat, stat)



