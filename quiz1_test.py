#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:30:16 2018

@author: chrisconroy
"""

import numpy as np # import numpy package for calculations
import matplotlib.pyplot as plt 

M =np.random.normal(0,1,(1*10))
M=np.reshape(M, (10,1000))
M_Idx = np.shape(M)


def Fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1)+Fib(n-2)
    
Sequence = np.zeros(10)    

for k in range(1,10):
    Sequence[k]=Fib(k)