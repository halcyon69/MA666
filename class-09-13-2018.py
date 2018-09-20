#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 12:49:06 2018

@author: chrisconroy
"""

import numpy as np # import numpy package for calculations
import matplotlib.pyplot as plt 

vector1 = np.array(np.linspace(0,10,11))
vector2 = np.array(np.linspace(0,10,11))
vector3 = np.array(np.linspace(0,10,11))
matrix1 = np.vstack((vector1,vector2,vector3))
indices_matrix1 = np.shape(matrix1)

matrix2 = np.zeros(indices_matrix1)

for k in range(0, (indices_matrix1[0])):
    for x in range(0, (indices_matrix1[1])):        
        matrix2[k,x] = (matrix1[k,x]+np.random.randn())*np.random.randn()

for k in range(0, (indices_matrix1[0])): # loop through each row of the matrix and plot the row vector
    plt.scatter(matrix2[k,:], np.linspace(1, indices_matrix1[1], indices_matrix1[1]), label="Row " + str(k+1))
plt.legend()

def matrix_multiplier(x,c):
    # takes an input vector, matrix, whatever, and multiplies it by a constant c and then plots the resulting values in a histogram
    values_hist = plt.hist(x*c) # plot all values of the matrix as histogram
    return values_hist


mu = 10
sigma = 2
x = np.random.normal(mu,sigma,1000) # normally distributed values
fs = 44100
duration = 2
t = np.linspace(0,2,fs*duration)



from scipy.stats import linregress # package to get slope of a line
linregress(x,y) # will give me the slope



def noise_matrix(x,t):
    """ Take an n-element vector of amplitue values and create an n-component signal (spectral profile) with those amplitudes
        and a time t (in seconds)
    """
    # Keep going
    return noise_waveforms





    
    
    
    
    
    