library(tictoc)
library(arrow)

# Read csv file using pandas and get time of read file in [s]
start_time = tic()
df_1 <- read.csv("sample.csv")
stop_time = toc()
print(paste('The csv read took ',gsub(" sec elapsed","",stop_time$callback_msg),'seconds'))

# Read parquet file using pandas and get time of read file in [s]
start_time = tic()
df_2 <- read_parquet("sample.parquet")
stop_time = toc()
print(paste('The parquet read took ',gsub(" sec elapsed","",stop_time$callback_msg),'seconds'))


