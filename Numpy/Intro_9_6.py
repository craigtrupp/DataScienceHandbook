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
print('hey')
# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)

# Create a 3x3 array of uniformly distributed values, random values between 0 and 1
np.random.random((3,3))

# Create a 3x3 array of normally distributed random valuewith mean 0 and standard deviation 1
np.random.normal(0, 1, (3, 3))

# Create a 3x3 array of random integers in the interval [0, 10]
np.random.randint(0,10, (3,3))

# Create a 3x3 identity matrix
np.eye(3)

# Create an uninitialized array of three integers
np.empty(3)


np.random.seed(19)

# One-dimensional array
x1 = np.random.randint(10, size=6)
# Two-dimensional array
x2 = np.random.randint(10, size=(3,4))
# Three - dimensional array
x3 = np.random.randint(10, size=(3,4,5))

print([[x.ndim, x.shape, x.size] for x in [x1,x2,x3]])
print(x2)
print(x3)

# Array Indexing 2D and 3D (Sets)
x2[1, -1]
x2[-1, 1]

# Get 7 with negative indexing (& positive) in third set, second to last array
x3[-1, -2, -2]
x3[2,2,3]

# Array Slicing : Accessing Subarrays
# x[start:stop:step]
x = np.arange(11, dtype=int)

# elements after index 5
x[5:]

# every other element
x[::2]

# every other elements .. odds for range
x[1::2]

# negative step used results in (start and stop are swapped for slice syntax) : trick to reverse
x[::-1]

# reversed every other from index 5
x[5::-2]

# Multidimensional

#rows slice, column slice
x2[:2, :2]

# Reversed together
x2[::-1, ::-1]

# pull column for all rows
x2[:, 0]

# first row of nd array
x2[0, :]


# Subarray as no-copy views
x2_sub = x2[:2, :2]
x2_sub
# Modify view
x2_sub[0, 0] = 99

x2_sub
x2

# See how the first index position updated in our view is updated from the original

# Using .copy() method to avoid mutation
x2_sub_copy = x2[:2, :2].copy()
x2_sub_copy
x2_sub_copy[0, 0] = 42
x2_sub_copy
x2

# Notice how the copy allows for mutation on created variable to not impact the array used to create the copy

