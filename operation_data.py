#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 01:27:59 2022

@author: anthelme
"""

import lib_math as lb 


import numpy as np
import pandas as pd


def replace_missing_values_by_mean(df):
    new_df = pd.DataFrame()
    for feature in df:
        mean = lb.ft_mean(df[feature])
        n = lb.ft_count(df[feature])
        new_df[feature] = df[feature]
        for i in range(n):
            if df[feature][i]!= df[feature][i]:
                new_df[feature].loc[i] = mean
    return new_df
                
def replace_missing_values_by_zeros(df):
    new_df = pd.DataFrame()
    for feature in df:
        n = lb.ft_count(df[feature])
        new_df[feature] = df[feature]
        for i in range(n):
            if df[feature][i]!= df[feature][i]:
                new_df[feature].loc[i] = 0
    return new_df
                
def standardize(X, mean, std):
    return (X - mean) / std

def norm_values(df):
    std_df = pd.DataFrame()
    for col in df:
        mean = lb.ft_mean(df[col])
        std = lb.ft_std(df[col])
        std_df[col] = standardize(df[col], mean, std)
      
    return std_df
        