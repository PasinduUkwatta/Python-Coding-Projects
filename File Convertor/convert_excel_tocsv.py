# importing pandas as pd
import pandas as pd

# Read and store content
# of an excel file
read_file = pd.read_excel("C:/Users/Acer/Desktop/test.xlsx")

# Write the dataframe object
# into csv file
read_file.to_csv("C:/Users/Acer/Desktop/Test.csv",
                 index=None,
                 header=True)

# read csv file and convert
# into a dataframe object
# df = pd.DataFrame(pd.read_csv("Test.csv"))
#
# # show the dataframe
# df