import pandas as pd

df = pd.read_csv('dwarf_stars.csv')

df = df.dropna()

df.Mass = df.Mass.str.replace('[^a-zA-Z0-9]','').astype('float')

df["Radius"] = df["Radius"] * (0.102763)

df["Mass"] = df["Mass"]*(0.000954588)

print(df.head(10))

df.to_csv('unit_converted_stars.csv')

df2 = pd.read_csv('bright_stars.csv')

df2.dropna()

new_df = pd.read_csv('unit_converted_stars.csv')

final_stars_df = pd.merge(df2,new_df)