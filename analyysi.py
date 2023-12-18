import pandas as pd
import os

filepaths = [os.path.join("data", x) for xs in os.walk("data") for x in xs[2]]
dfs = [pd.read_csv(path) for path in filepaths]
df = pd.concat(dfs)

print(df.groupby("väri").count())
