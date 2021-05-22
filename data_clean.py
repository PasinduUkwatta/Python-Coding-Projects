import numpy as np

import pandas as pd

used_car_data_set=pd.read_csv("vehicles_final.csv")
(used_car_data_set)

used_car_data_set.T

used_car_data_set.info()

used_car_data_set.isna().sum()

used_car_data_set_drop =used_car_data_set.drop(["id","url","region_url","VIN","image_url","description","county","lat","long","posting_date"],axis=1)
used_car_data_set_drop

used_car_data_set_drop.info()

used_car_data_set_drop.isna().sum()
