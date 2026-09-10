import sys
print("arguments", sys.argv)

day = int(sys.argv[1])


import pandas as pd

df = pd.DataFrame({"Day": [1, 2], "Number_Passengers": [3, 4]})
df["day"] = day
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
print(f"Running pipeline for day {day}")