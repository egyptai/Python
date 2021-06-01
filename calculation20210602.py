# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:58:24 2021

@author: dms10
"""

import random

a = random.randint(1, 30)
b = random.randint(1, 30)

print(a, "+", b, '=')
x = input()
c = int(x)

if a + b == c:
    print("천재!")
else:
    print("바보")