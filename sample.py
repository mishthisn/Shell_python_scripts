import csv

stock_dictionary = {}

with open("stock_value") as fp:
    csv_reader = csv.reader(fp, delimiter=",")

    print(csv_reader)

    for row in csv_reader:
        print(row)

    for row in csv_reader:
        stock = row[0]
        if stock in stock_dictionary.keys():
            stock_dictionary[stock] += 1
        else:
            stock_dictionary[stock] = 1

    for i in stock_dictionary.items():
        print("{0} = {1}".format(i[0], i[1]))
