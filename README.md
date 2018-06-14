# xls-to-aws-s3
extracts data from XLS files to CSV files, converts time columns to specified datetime format, loads files to AWS S3 bucket <br>
<br>
Usefull for scenerios when 2 separate files are dropped to a start_folder (usually by client/vendor) <br>
Code scans start_folder for files by respective filename identifiers <br>
Each File.xls is read, a dataframe is created of each file's data from specified sheet, skipping any applicable header rows <br>
Each specified 'date_column' reformatted to specified datetime format <br>
Note: Python 2.7 defaults to ascii encoding, Python 3 defaults to utf-8 <br>
Each dataframe is saved as File.csv in a specified homebase folder <br>
<br>
AWS S3 connection made <br>
Code scans homebase folder for files by identifier <br>
Code uploads each File.csv to respective specified S3 buckets <br>
