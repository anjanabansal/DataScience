# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:03:28 2022

@author: Anjana.Bansal
"""

import matplotlib.pyplot  as plt;


# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10];

# plt.bar(movies,num_oscars);
# # plt.xticks(movies
# plt.show();


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorite Movies") # add a title
plt.ylabel("# of Academy Awards") # label the y-axis
# label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)
plt.show()


plt.plot(range(len(num_oscars)),num_oscars,'g-',label = 'num of oscars');
plt.show();


