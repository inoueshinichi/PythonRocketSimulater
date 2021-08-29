#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:17:27 2017

@author: inoueshinichi
"""

""" prun2.py """

import numpy as np
from memory_profiler import profile


@profile # 次の関数はメモリプロファイラの分析対象とする
def func_a():
    a = np.random.randn(500, 500)
    return a**2


@profile # 次の関数はメモリプロファイラの分析対象とする
def func_b():
    a = np.random.randn(1000, 1000)
    return a**2


def func_both():
    a = func_a()
    b = func_b()
    return [a, b]

if __name__ == '__main__':
    func_both()