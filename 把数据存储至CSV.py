import csv
with open('lianjia.csv', 'r', encoding='UTF-8') as csvfile:
    #csv_reader把每一行数据转化成了一个列表，列表中从左至右每个元素是一个字符串
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
