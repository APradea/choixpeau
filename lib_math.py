#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:14:01 2022

@author: anthelme
"""

import numpy as np
    
def ft_sum(tab):
    somme = 0
    
    for value in tab:
        if value == value : 
            somme += value
    return somme

def ft_count(tab):
    cnt = 0
    
    for x in tab:
        cnt += 1
    return cnt 
    
def ft_mean(tab):
    somme = 0
    counter = 0
    for value in tab:
       
        if value == value : 
            counter += 1
            somme += value

    return somme / counter

def ft_std(tab):
    
    somme = 0
    mean = ft_mean(tab)
    counter = 0
    for value in tab:
       
        if value == value : 
            counter += 1
            somme += (value - mean) **2 
            
    variance = somme / counter
            
    return np.sqrt(variance)


def ft_max(tab):
    
    le_max = tab[0]
    for x in tab:
        if x > le_max:
            le_max = x
            
    return le_max

def ft_min(tab):
    le_min = tab[0]
    for x in tab:
        if x < le_min:
            le_min = x
            
    return le_min

def first_quartile(tab):
    
    n = ft_count(tab)
    rank = (n + 3)// 4
    tab_sort = np.sort(tab)
    
    if (n  + 3) % 4 == 0 :
        return tab_sort[rank - 1]
    elif (n  + 3) % 4 == 1 : 
        return (tab_sort[rank - 1] * 3 + tab_sort[rank]) / 4 
    elif (n  + 3) % 4 == 2 : 
        return (tab_sort[rank - 1] + tab_sort[rank]) / 2
    elif (n  + 3) % 4 == 3 : 
        return (tab_sort[rank - 1] + tab_sort[rank] * 3) / 4

def third_quartile(tab):
    
    n = ft_count(tab)
    rank = (3 * n + 1)// 4
    tab_sort = np.sort(tab)
    
    if (3 * n + 1) % 4 == 0 :
        return tab_sort[rank - 1]
    elif (3 * n + 1) % 4 == 1 : 
        return (tab_sort[rank - 1] * 3 + tab_sort[rank]) / 4 
    elif (3 * n + 1) % 4 == 2 : 
        return (tab_sort[rank - 1] + tab_sort[rank]) / 2
    elif (3 * n + 1) % 4 == 3 : 
        return (tab_sort[rank - 1] + tab_sort[rank] * 3) / 4

def median(tab):
    n = ft_count(tab)
    rank = (n + 1) // 2
    tab_sort = np.sort(tab)
    if (n + 1)  % 2 != 0:
        return (tab_sort[rank - 1] + tab_sort[rank]) / 2 

    return tab_sort[rank - 1]

def euclidian_distance(X,Y):
    somme = 0
    for x in X:
        if x == x :
            for y in Y:
                if y == y :
                    somme = (x - y)**2
    return np.sqrt(somme)
