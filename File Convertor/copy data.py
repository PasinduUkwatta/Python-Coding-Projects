import csv

data = []
with open('C:/Users/Acer/Desktop/BigDataSet/vehicles.csv', 'r',encoding="utf8") as f:
    f_csv = csv.reader(f)
    # header = next(f_csv)
    for row in f_csv:
        data.append(row)


# write
with open('C:/Users/Acer/Desktop/vehicles_new.csv', 'w+',encoding="utf8") as f:
    writer = csv.writer(f)
    for i in range(int(len(data) * 25 / 100)):
        writer.writerow(data[i])