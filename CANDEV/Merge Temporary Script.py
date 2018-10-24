#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:46:38 2018

@author: gobindbirsingh
"""

import shutil

#import csv files from folder
allFiles = [f for f in os.listdir('.') if os.path.isfile(f)]
with open('someoutputfile.csv', 'wb') as outfile:
    for i, fname in enumerate(allFiles):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()  # Throw away header on all but first file
            # Block copy rest of file from input to output without parsing
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")
            
print (allFiles)

df = pd.DataFrame()
for file_ in allFiles:
    file_df = pd.read_csv(file_,sep=',', parse_dates=[0], infer_datetime_format=True,header=None ,encoding = "ISO-8859-1")
    file_df['file_name'] = file_
    df = df.append(file_df)
df.to_csv('out.csv')
print(df)
