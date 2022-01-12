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
perMillionFig =  10000000

MergedData = statesData.merge(agg,left_on='State',right_on='State/UnionTerritory')
print(MergedData);
MergedData['PerMillion'] = (MergedData['Confirmed']/MergedData['Area (per sq km)'])*perMillionFig;
print(MergedData['PerMillion']);

print(indiv.columns);
a = indiv['nationality'].unique();
print(type(a));
b = (np.isin(["India","INDIAN"],a));
print (b);

# condition = a[a.isin(["India","INDIAN"])];
# print(indiv[condition]);



#Count the number of males and females.
numOfMalesAndFemales = indiv['gender'].value_counts();
print(numOfMalesAndFemales);

a = indiv['detected_state'].groupby(indiv['gender'].value_counts()).count();
a = indiv['gender'].groupby(indiv['detected_state'].value_counts()).count();
a= indiv.groupby(['detected_state','gender']).size();
print(a);
at = (td['Cured'].groupby(td['State/UnionTerritory'])).sum();
print((at));


# State with maximum recoveries.
StateWithMaxRecoveries = at.idxmax();
print(StateWithMaxRecoveries);


at1 = (indiv['gender'].groupby(indiv['detected_state'])).value_counts();
print(at1);

# a = [[1,2],[3,4],[5,6],[7,8]];
# b = pd.DataFrame((a),index=['a1','a2','a3','n4'],columns = ['c1','c2']);
# print(b);
# print(b.a1)
# print(b[['c1']])
# print(b[['c1']].filter(like='a')).head();
# print(b[b[]]);
d = td.groupby(['Date','Time','Confirmed']).size();
e = td['Confirmed'].groupby(td['Date']).sum();       
print(e );
