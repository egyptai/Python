# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:02:31 2021

@author: dms10
"""

s = 0
for x in range(1,11):
    s = s + x
    print("x:", x, "sum:", s)
    
s = 0
x = 1
while x <= 10:
    s = s + x
    print("x:", x, "sum:", s)
    x = x + 1