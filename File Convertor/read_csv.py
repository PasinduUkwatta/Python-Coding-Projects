import pandas as pd
import csv

reviews_df = pd. read_csv("C:/Users/Acer/Desktop/Test.csv", nrows=100)
print("Dataframe shape:", reviews_df.shape)



csvfile = open('C:/Users/Acer/Desktop/Test.csv', 'r')
reader = csv.reader(csvfile)

with open('C:/Users/Acer/Desktop/test_write.csv', "w+") as csv_file1: # different variable
    writer = csv.writer(csv_file1)

    for row in reader:
        if row in range (100):
            print(row.count())
            # writer.writerow(row)