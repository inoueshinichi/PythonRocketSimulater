#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:59:42 2017

@author: inoueshinichi
"""

""" fc.py """

import numpy as np
n = 20

def func_c():
    A = np.arange(0, n*n).reshape(n, n) + np.identity(n)
    b = np.arange(0, n)
    x = np.dot(np.linalg.inv(A), b)
    