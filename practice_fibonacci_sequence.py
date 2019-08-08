# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:46:08 2019

@author: S69862
"""

'''
1
1
2

3
5
8
13
21
'''

first, second= 0, 1

for x in range(1,20):  
    
            
    next_sum = first + second
    
    print(next_sum)
    
    first = second
    second = next_sum
    
  