# -*- coding: utf-8 -*-
"""
@author: Joseph
"""

import pandas as pd
import glob
import os

## type in pathway of file location 
path = r'E:\Documents\Python\combine these sheets pls\'

## searching for all the excel files within specific file location
filenames = glob.glob(path + "/*.xlsx")

## Note: ensure all column headers are the same

## dataframe initialisation
concat_sheets_multiple_file = pd.DataFrame()

for file in filenames:
    df = pd.read_excel(file, sheet_name=None, skiprows=None, nrows=None, usecols=None, index_col=None)
    concat_sheets_single_file = pd.concat(df,sort=False)
    #append file name in a column
    concat_sheets_single_file['filename'] = os.path.basename(file)
    #append command to stack prev concatenated data on top of each other 
    concat_sheets_multiple_file = concat_sheets_multiple_file.append(concat_sheets_single_file)
    
## Write consolidated data into excel file
consolidate = pd.ExcelWriter('combined_file_python.xlsx')
