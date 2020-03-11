# 100-199
# 200-399
# 400-500
# 1. Open the file and print the first line

import csv

company_server_log_array = ["Ip","Date","UserNo","page","ResponseCode","No","Time"]

my_dict = {}
my_dict.keys()
my_dict.values()
my_dict.items()

with open("csv_server_log.csv") as fp:
    csv_reader = csv.reader(fp, delimiter=",")
    print(csv_reader)
    #next(fp)
    for row in csv_reader:
        url = row[0]
        if url in my_dict.keys():
            my_dict[url] += 1
        else:
            my_dict[url] = 1

    for i in my_dict.items():
        print("{0} = {1}".format(i[0], i[1]))



