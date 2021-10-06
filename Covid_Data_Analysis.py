# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp


td = pd.read_csv(r'covid_19_india.csv');
newtd = td.loc[:,~td.columns.isin(['Sno','Date','Time','State/UnionTerritory'])];
#print(newtd.mean);
#print(newtd.median);
#Q1 = pd.percentile(newtd,25);
#Q2 = pd.percentile(newtd,50);
#Q3 = pd.percentile(newtd,75);
#Q4 = pd.percentile(newtd,95);
#print(Q1);
#print(Q3);
a = (td.describe([.25,.50,.75,.95,.99]));
print(a.loc['25%']['Confirmed'])
iqr = (a.loc['75%']['Confirmed'] - a.loc['25%']['Confirmed'])

#apply condition on confirmed column where the values are outliers and then display those values in a separate column named as Outlier
highOutlier = (td.loc[(td['Confirmed'] > (a.loc['75%']['Confirmed'] + iqr))]);
print(highOutlier)
print(highOutlier['State/UnionTerritory'].unique())
#b.rename(columns={"Confirmed":"Outlier"})
#print(a(['Confirmed'] > (a.loc['75%']['Confirmed'] + iqr)]))
#print(td.mean(1));
