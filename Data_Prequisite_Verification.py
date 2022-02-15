# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:45:21 2022

@author: Anjana.Bansal
"""

#Small form application data cleaning
#https://github.com/microsoft/Data-Science-For-Beginners/blob/4b51b11df6a9a11265c9cf507f579ed911190d61/data/form.csv

import pandas as pd;


formData = "C:\\Users\\anjana.bansal\\Documents\\FormData.csv"
td = pd.read_csv("C:/Users/anjana.bansal/Documents/DataScience-main/covid_19_india.csv");


# print(td.describe());
tdFormData = pd.read_csv(formData);

# #print(tdFormData);
# #print(tdFormData.shape);
# #print(tdFormData.columns);
# print(tdFormData.info());
# print(tdFormData.describe());
# print(tdFormData.isnull());
# print(tdFormData.isnull().sum());
# # print(tdFormData.tail);
# print(tdFormData.dropna(0,how='all'));
# tdFormData.dropna?
# print(tdFormData);
# print(tdFormData.loc['birth_month']);

# print(tdFormData[['birth_month','state']].fillna(method = 'ffill'));
# print(tdFormData);

# print(tdFormData[['birth_month','state']].fillna(method = 'bfill'));
# print(tdFormData[['birth_month','state']].fillna('Jan',inplace=True));
newpd = (tdFormData.fillna(method = 'ffill'));
secondPd = newpd.fillna(method='bfill');
print(secondPd);

print (secondPd.duplicated());
