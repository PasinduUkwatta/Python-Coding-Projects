import pandas as pd

read_file = pd.read_csv (r'C:\Users\Acer\Desktop\text-query-tweets.csv')
read_file.to_excel (r'C:\Users\Acer\Desktop\text-query-tweets.xlsx', index = None, header=True)