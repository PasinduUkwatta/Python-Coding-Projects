import csv

with open('C:/Users/Acer/Desktop/vehicles_new.csv',encoding="utf8") as input, open('C:/Users/Acer/Desktop/vehicles_final.csv', 'w',encoding="utf8") as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)