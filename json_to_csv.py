import pandas as pd
df = pd.read_json (r'C:\Users\Acer\Desktop\New folder\wing_commander_abhinandan_feb14_march_31_split0.json')
df.to_csv (r'C:\Users\Acer\Desktop\New folder\wing_commander_abhinandan_feb14_march_31_split0.csv', index = None)