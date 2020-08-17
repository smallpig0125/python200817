# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:15:44 2020

@author: user
"""
A_score = int(input("數學成績:"))
B_score = int(input("英文成績:"))
if A_score <=100 and A_score >=0 and \
   B_score <=100 and B_score >=0:
   if A_score and B_score >=90:
    print("good")
   elif A_score and B_score <60:
    print("bad")

else:
    print("下次加油")