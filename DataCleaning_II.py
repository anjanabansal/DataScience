# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:30:15 2022

@author: Anjana.Bansal
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:26:28 2022

@author: Anjana.Bansal
"""

import pandas as pd;
from mlxtend.preprocessing import minmax_scaling;
from scipy import stats
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

td = pd.read_csv(r'C:\Users\anjana.bansal\Documents\Kaggle\Data Cleaning\ks-projects-201801.csv');

# print(td.shape);
# print(td.columns);
# print(td.info());
# print(td['usd_goal_real']);
td1 =  pd.DataFrame(td['usd_goal_real']);
# print(td1);
a = minmax_scaling(td1,['usd_goal_real']);
# print(a);
b = td['usd_goal_real'] > 1533.95;
# print(b);
# print(type(b));
c = td['usd_goal_real'].loc[b];
# print(c);

d = stats.boxcox(c);
print(d);
e = pd.Series(d[0],index = c.index);
print(e);
# print(td.isnull());
# ntd = (td.dropna(axis=1));
# print(ntd.isnull().sum());
# mtd = td.fillna(0);
# print(mtd);
# print(mtd.dropna(axis=1));
# print(td.isnull().all());