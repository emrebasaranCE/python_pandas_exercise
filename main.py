import pandas as pd

line_seperator = "---------------------------------"
print("Pandas Version: " + pd.__version__)

csv_path = "data.csv"

df = pd.read_csv(csv_path)

print(line_seperator)
print('Reading specific data with dataset["Duration"][1]:')
print(df["Duration"][1].__str__())

print(line_seperator)
print("Get the specific row with dataset.loc[2]:")
print(df.loc[2])