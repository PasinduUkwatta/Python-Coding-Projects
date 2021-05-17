import csv

csvfile = open('C:/Users/Acer/Desktop/Test.csv', 'r')
reader = csv.reader(csvfile)

with open('C:/Users/Acer/Desktop/test_write.csv', "w+") as csv_file1: # different variable
    writer = csv.writer(csv_file1, delimiter=',')

    for row in reader:
        if row in range (100):
            # print(row)
            writer.writerow(row)