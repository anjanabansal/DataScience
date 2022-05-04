# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:26:28 2022

@author: Anjana.Bansal
"""

import pandas as pd;
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
td = pd.read_csv(r'C:\Users\anjana.bansal\Documents\Kaggle\Data Cleaning\NFL Play by Play 2009-2016 (v3).csv');

# print(td.shape);
# print(td.columns);
# print(td.info());
# print(td.isnull());
# ntd = (td.dropna(axis=1));
# print(ntd.isnull().sum());
# mtd = td.fillna(0);
# print(mtd);
# print(mtd.dropna(axis=1));
print(td.isnull().all());