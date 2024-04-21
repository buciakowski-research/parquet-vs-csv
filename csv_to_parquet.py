import pandas as pd

df = pd.read_csv('sample.csv')
df.to_parquet('sample.parquet',engine='pyarrow')