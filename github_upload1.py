#import xlrd
#import unicodecsv as csv
#import sys
import tinys3
import os
import glob
import fnmatch
import pandas as pd
from datetime import datetime

#define variables
file1 = 'INSERT FILE1 NAME'
file2 = 'INSERT FILE2 NAME'
start_folder = 'INSERT PATH TO FOLDER WITH FILE1 & FILE2'
middle_folder = 'INSERT PATH TO FOLDER USED AS HOMEBASE'
end_folder_file1 = 'INSERT PATH TO FILE1 S3 BUCKET'
end_folder_file2 = 'INSERT PATH TO FILE2 S3 BUCKET'
default_bucket = 'INSERT ROOT S3 BUCKET NAME'
s3_access_key = 'INSERT S3 ACCESS KEY'
s3_secret_key = 'INSERT S3 SECRET KEY'

#searches start_folder for file1.xls & file2.xls by thier respective identifiers to be inputted below
#reads file1.xls & file2.xls from start_folder, converts date column to datetime format, saves as file1.csv & file2.csv
for filename in glob.glob(os.middle_folder.join(start_folder, '*INSERT FILE1 & FILE2 NAME IDENTIFIER*')):
    if fnmatch.fnmatch(filename, '*INSERT FILE1 NAME IDENTIFIER*'):
        df1 = pd.read_excel(start_folder + file1 + '.xls', header=6) #for header enter number of rows to be skipped
        pd.to_datetime(df1['INSERT COLUMN NAME TO BE CONVERTED TO DATETIME'], format="%Y-%m-%d %H:%M:%S.%f") #use format that matches your data
        df1.to_csv(middle_folder + file1 + '.csv', encoding='utf-8', index=False) #encoding defaults to ascii in python2.7 if not specified
    elif fnmatch.fnmatch(filename, '*INSERT FILE2 NAME IDENTIFIER*'):
        df2 = pd.read_excel(start_folder + file2 + '.xls', header=10) #for header enter number of rows to be skipped
        pd.to_datetime(df2['INSERT COLUMN NAME TO BE CONVERTED TO DATETIME'], format='%Y-%m-%d %H:%M:%S.%f') #use format that matches your data
        df2.to_csv(middle_folder + file2 + '.csv', encoding='utf-8', index=False) #encoding defaults to ascii in python2.7 if not specified
    else:
        pass

#set up AWS S3 connection for upload
conn = tinys3.Connection(s3_access_key, s3_secret_key, default_bucket ,tls=True)

#upload file1.csv & file2.csv from folder used as homebase to final S3 folders
for filename in glob.glob(os.path.join(middle_folder, '*weekly*')):

    if fnmatch.fnmatch(filename, '*file1*.csv'):
        f = open(middle_folder + file1 + '.csv', 'rb')
        conn.upload(end_folder_file1 + file1 + '.csv', f)
    elif fnmatch.fnmatch(filename, '*file2*.csv'):
        g = open(middle_folder + file2 + '.csv', 'rb')
        conn.upload(end_folder_file2 + file2 + '.csv', g)
    else:
        pass