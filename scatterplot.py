#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:34:18 2022

@author: anthelme
"""

import pandas as pd
import numpy as np
import sys
import lib_math as lb
import operation_data
import argparse
import matplotlib.pyplot as plt


def create_scatter(df, x, y, scatter_plot=False):
    
    
    if not scatter_plot:
        scatter_plot = plt.subplot()
    
    scatter_plot.scatter(df[x].loc["Gryffindor"], df[y].loc["Gryffindor"], color='red', alpha=0.5)
    scatter_plot.scatter(df[x].loc["Hufflepuff"], df[y].loc["Hufflepuff"], color='yellow', alpha=0.5)
    scatter_plot.scatter(df[x].loc["Ravenclaw"], df[y].loc["Ravenclaw"], color='blue', alpha=0.5)
    scatter_plot.scatter(df[x].loc["Slytherin"], df[y].loc["Slytherin"], color='green', alpha=0.5)
    
    return scatter_plot
    
    

def scatter(norm, course1, course2):

    # on ouvre le document et on met les maisons en index et on ne garde que les valeurs numeriques
    df = pd.read_csv("./datasets/dataset_train.csv", index_col = "Hogwarts House").select_dtypes("number")
    # on supprime la colone Index du document
    df = df.drop('Index', axis = 1)

    if norm == 1:
        operation_data.norm_values(df)
        
    scatter_plot = create_scatter(df, course1, course2)
    
    scatter_plot.set(xlabel = course1, ylabel=course1)
    scatter_plot.legend(['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--norm", type = int, help="can be set as true or false", default= 0)
    parser.add_argument("--course1", type = str, help="enter the first course you want", default= 'Astronomy')
    parser.add_argument("--course2", type = str, help="enter the second course you want", default= 'Defense Against the Dark Arts')
    args = parser.parse_args()
    norm = 0
    if args.norm and args.norm == "true":
        norm = 1
        print(args.norm)
    course1 = args.course1
    course2 = args.course2
    scatter(norm, course1, course2)
