#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:32:48 2017

@author: inoueshinichi
"""

def my_add(x, y):
    """２つの数字を加算する"""
    out = x + z # バグ: zという変数は定義されていない
    return out + y
    
if __name__ == "__main__":
    a, b = 3, 4
    z = my_add(a, b)
    print(z)