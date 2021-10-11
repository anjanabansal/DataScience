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



td = pd.read_csv(r'testData.csv');
aggConfirmed_State = (td['Confirmed'].groupby(td['State/UnionTerritory'])).sum();
agg =  aggConfirmed_State
print(agg);
statewise = (td['Confirmed'].groupby(td['State/UnionTerritory']).sum()).describe();
# print(statewise);
iqr = statewise['75%'] - statewise['25%']
high = statewise['75%']+iqr*1.5;
low = statewise['25%'] - iqr*1.5;
print(iqr);
print( high);
print(low);
highoutlier = agg[agg > high];
lowoutlier = agg[agg < low];
print(highoutlier);
print(lowoutlier);