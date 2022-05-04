# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:44:58 2022

@author: Anjana.Bansal
"""

"""Mastermind
Generate a random four digit number. The player has to keep inputting four digit numbers until they guess the randomly generated number. After each unsuccessful try it should say
how many numbers they got correct, but not which position they got right. At the end of the game should congratulate the user and say how many tries it took."""
import random;

def verifyEnteredNum(num,myNumber):
    enterednum = str(num);
    l=[];
    my=[];
    for u in enterednum:
         l.append(int(u));
    p =  str(myNumber);
    for y in p:
         my.append(int(y));
    print(l);
    print(my);
    # new  = enterednum.split('').join();
   
    # print((enterednum)[0]);
    cnt =0;
    # print(type(num));
    for x,y in zip(my,l):
       
        # print(type(x));
        # print(type(y));
        print(x);
        print(y);
        if x == y:
            cnt = cnt + 1;
            # print("matching");
    
    return cnt;

   
l = range(5000,5489,1);
print(type(l));
z = random.sample(l,1);
print(z);
myNumber  = z;
print(type(myNumber));
player = [[],[],[],[]];
correct =[];
tries =0;
win =False;
while(win !=True and tries <=10):
    enteredNum = input("Please guess four digit number by entering: ")
    l= verifyEnteredNum(enteredNum,myNumber);
    
    if (l < 4):
        correct.append(l);
        print(f"You got {l}  numbers correct");
    else:
        win = True;
        print("Congratulations");
        tries = len(correct) + 1;
        print(f"You tried {tries} number of times");

        
# verifyEnteredNum(1456,myNumber);          
    # player[0].append(enterednum[0]);
    # player[1].append(enterednum[1]);
    # player[2].append(enterednum[2]);
    # player[3].append(enterednum[3]);
    # if (enterednum == player)