import pandas as pd
import time

# Read csv file using pandas and get time of read file in [s]
start_time = time.time()
df_1 = pd.read_csv('sample.csv')
stop_time = time.time()
print('The csv read took %s seconds' %(stop_time - start_time))


# Read parquet file using pandas and get time of read file in [s]
start_time = time.time()
df_2 = pd.read_parquet('sample.parquet', engine='pyarrow')
stop_time = time.time()
print('The parquet read took %s seconds' %(stop_time - start_time))