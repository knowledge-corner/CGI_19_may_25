import pandas as pd

df = pd.read_csv("./datasets/auto-mpg.csv")
df = df.loc[df.horsepower.str.isdigit()]
df.horsepower = df.horsepower.astype(int)
df.origin = df.origin.map({1 : "USA", 2 : "Germany", 3 : "Japan"})

def avg_mpg_by_cyl(dff):
    result = dff.groupby("cylinders")["mpg"].mean().to_frame().round(2).reset_index()
    return result
