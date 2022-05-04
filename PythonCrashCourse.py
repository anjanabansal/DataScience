# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:17:16 2022

@author: Anjana.Bansal
"""

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]


# How many sites are there?
    

print(len(data));

# How many birds were counted at the 7th site?

print(data[6][1]);
# How many birds were counted at the last site?
print(data[-1][1])
# What is the total number of birds counted across all sites?

def getNum(data):
    sum =0;
    for x in data:
        sum = sum + x[1];
    return sum;
print(getNum(data));
# What is the average number of birds seen on a site?
print((getNum(data)/len(data)));
# What is the total number of birds counted on sites with codes beginning with C? (don’t just identify this sites by eye, in the real world there could be hundreds or thousands of sites)
import re
def getSpecSum(data):

    specSum =0;
    for i,item in enumerate(data):
        if re.match('C',data[i][0]):
           specSum = specSum + data[i][1];
    return specSum;

print(getSpecSum(data));
