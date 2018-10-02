import csv

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    timestamps = []
    unit = []

    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)





#id,ts,event,unit,man_fwd,man_back,main_flush,main_bag_used,second_flush,second_bag_used,bag_used,bag_left,blockages,resets,fault
