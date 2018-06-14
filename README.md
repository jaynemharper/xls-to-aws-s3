# xls-to-aws-s3
# extracts data from XLS files to CSV files, converts time columns to specified datetime format, loads files to AWS S3 bucket

# Usefull for scenerios when 2 separate files are dropped to a start_folder (usually by client/vendor)
# Code scans start_folder for files by respective filename identifiers
# Each File.xls is read, a dataframe is created of each file's data from specified sheet, skipping any applicable header rows
# Each specified 'date_column' reformatted to specified datetime format
# Note: Python 2.7 defaults to ascii encoding, Python 3 defaults to utf-8
# Each dataframe is saved as File.csv in a specified homebase folder

# AWS S3 connection made
# Code scans homebase folder for files by identifier
# Code uploads each File.csv to respective specified S3 buckets
