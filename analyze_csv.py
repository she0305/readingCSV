import csv

with open('World_Airports.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    next(csv_reader)
    for line in csv_reader:
        print(line)
        break
