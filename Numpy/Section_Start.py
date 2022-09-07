#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:13:14 2022

@author: craigrupp
"""
# Pre Numpy Lessons / IPython Ref (Revisit Book)
# =============================================================================
# def say_hi_name(name='Tony'):
#     print(f"Hello our friend, {name}")
#     
# say_hi_name('Craig')
# say_hi_name()
# 
# import math
# math.sin(2)
# math.cos(2)
# print(In)
# print(Out)
# print(Out[__2])
# =============================================================================

import numpy as np

# range function from i to i + 3 for each index in the list (numpy list comprehension)
np.array([range(i, i + 3) for i in [2,4,6]])
print([[range(i, i + 3)] for i in [2,4,6]])
# Non numpy type 2D list wiht list comprehension in a list comprehension 
print([[i for i in range(i, i + 3)] for i in [2,4,6]])
np.arange(0,20,2)

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)

# Create a 3x3 array of uniformly distributed values, random values between 0 and 1
np.random.random((3,3))
