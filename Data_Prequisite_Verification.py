# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:45:21 2022

@author: Anjana.Bansal
"""

#Small form application data cleaning
#https://github.com/microsoft/Data-Science-For-Beginners/blob/4b51b11df6a9a11265c9cf507f579ed911190d61/data/form.csv

import pandas as pd;
import matplotlib.pyplot as plt;

formData = "C:\\Users\\anjana.bansal\\Documents\\FormData.csv"
td = pd.read_csv("C:/Users/anjana.bansal/Documents/DataScience-main/covid_19_india.csv");


# # print(td.describe());
tdFormData = pd.read_csv(formData);

# #print(tdFormData);
# #print(tdFormData.shape);
# #print(tdFormData.columns);
# print(tdFormData.info());
# print(tdFormData.describe());
# print(tdFormData.isnull());
# print(tdFormData.isnull().sum());
# # print(tdFormData.tail);
print(tdFormData.dropna(0,how='all'));
# tdFormData.dropna?
# print(tdFormData);
# print(tdFormData.loc['birth_month']);

# print(tdFormData[['birth_month','state']].fillna(method = 'ffill'));
# print(tdFormData);

# print(tdFormData[['birth_month','state']].fillna(method = 'bfill'));
# print(tdFormData[['birth_month','state']].fillna('Jan',inplace=True));
# newpd = (tdFormData.fillna(method = 'ffill'));
# secondPd = newpd.fillna(method='bfill');
# print(secondPd);

# print (secondPd.duplicated());


'*************************************************'
# tdFormData  = pd.read_csv(r'C:\Users\anjana.bansal\Documents\owid-covid-data.csv\owid-covid-data.csv');

# print(tdFormData.shape);
# print(tdFormData.columns);
# print(tdFormData.info());
# a = tdFormData.info();
# a = tdFormData.loc[(tdFormData['total_cases'] > 0)]
# b = a.dropna(axis=1);
# print(b);
# # c = b.describe();
# # print(c);
# d = b.duplicated();
# print(b[(b.duplicated()!=True)]);


# ********************************************************

tdFormData = pd.read_csv(r'C:\Users\anjana.bansal\Documents\NFLX.csv');
print(tdFormData.shape);
print(tdFormData.columns);
print(tdFormData.info());
print(tdFormData.dropna(axis=1));
print(tdFormData.describe());
plt.title("Netflix");
plt.xlabel("Date");

plt.ylabel("High");
# plt.xticks(rotation=45);
x = tdFormData["Date"];
y = tdFormData["High"];
print(x.shape);
print(len(tdFormData));
###/This is the code to traverse the dataframe.
# for i in tdFormData["Date"].head():
#     print(i);
#     print(type(i));

'*********************************************************'
i=0;
for i in range(len(tdFormData)):
    x = tdFormData["Date"][i];
    y = tdFormData["High"][i];
    if (y > 700.630005):
        plt.plot(x,y,marker="*");
        plt.text(x, y, tdFormData["Date"][i]);
plt.show();

tdFormData["High"].plot(kind="hist",bins=10,figsize=(12,12));
plt.text();
plt.show();
# for i in x:
#     print(tdFormData["Date"][i]);
# for a in x:
#     print("hi " +  a);
# for i in y:
#     if i > 600:
#         plt.plot(x,y,"bo");
#         # plt.text(tdFormData, tdFormData[], s, kwargs)
# plt.plot(x,y,marker = "*",linestyle='dotted');
# plt.show();
# ********************************************************

# tdFormData = pd.read_csv(r'C:\Users\anjana.bansal\Documents\WineQT.csv');
# print(tdFormData.shape);
# print(tdFormData.columns);
# print(tdFormData.info());
# print(tdFormData.dropna(axis=0));
# plt.title("");




