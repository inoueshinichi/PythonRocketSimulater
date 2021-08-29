#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:08:58 2017

@author: inoueshinichi
"""

""" prun1.py """
import numpy as np

def func_a():
    a = np.random.randn(500, 500)
    return a ** 2
    
def func_b():
    a = np.random.randn(1000, 1000)
    return a ** 2
    
def func_both():
    a = func_a()
    b = func_b()
    return [a, b]
    
if __name__ == "__main__":
    func_both()
    
