import pandas as pd

# for i in range(0,7):
#     word =i
#     print(word)
#
#     json_file =f"wing_commander_abhinandan_feb14_march_31_split{word}.json"
#     csv_file =f"wing_commander_abhinandan_feb14_march_31_split{word}.csv"
#
#
#     df = pd.read_json (fr'C:\Users\Acer\Desktop\New folder\{json_file}')
#     df.to_csv (fr'C:\Users\Acer\Desktop\New folder\{csv_file}', index = None)
#

df = pd.read_json (fr'C:\Users\Acer\Desktop\New folder\wing_commander_abhinandan_feb14_march_31.json',lines=True)
df.to_csv (fr'C:\Users\Acer\Desktop\New folder\wing_commander_abhinandan_feb14_march_31.csv', index = None)