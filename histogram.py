#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:30:36 2022

@author: anthelme
"""

import pandas as pd
import numpy as np
import sys
import lib_math as lb
import operation_data
import argparse
import matplotlib.pyplot as plt


def create_histogram(df, course, histo=False):

    b = 50

    gryff = df.loc["Gryffindor"][course]
    huffle = df.loc["Hufflepuff"][course]
    raven = df.loc["Ravenclaw"][course]
    slyther = df.loc["Slytherin"][course]
    
    if not histo:
        histo = plt.subplot()

    histo.hist(gryff, bins = b, histtype="stepfilled", color = 'red',edgecolor = 'black', alpha = 0.5)
    histo.hist(huffle, bins = b, histtype="stepfilled", color = 'yellow', edgecolor = 'black', alpha = 0.5)
    histo.hist(raven, bins = b, histtype="stepfilled", color = 'blue', edgecolor = 'black' ,alpha = 0.5)
    histo.hist(slyther, bins = b, histtype="stepfilled" ,color = 'green', edgecolor = 'black', alpha = 0.5)
    
    return histo

def histogram(norm, course):

    # on ouvre le document et on met les maisons en index et on ne garde que les valeurs numeriques
    df = pd.read_csv("./datasets/dataset_train.csv", index_col = "Hogwarts House").select_dtypes("number")
    # on supprime la colone Index du document
    df = df.drop('Index', axis = 1)

    if norm == 1:
        operation_data.norm_values(df)
    if course == "all":
        for c in df:
            histo = create_histogram(df, c)
            histo.set(xlabel='Grades', ylabel='Number of Students', title='Repartition of grades in ' + c)
            histo.legend(['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])
            plt.show()
    else:
        histo = create_histogram(df, course)
        histo.set(xlabel='Grades', ylabel='Number of Students', title='Repartition of grades in ' + c)
        histo.legend(['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])
        plt.show()
    
     

    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--norm", help="can be set as true or false")
    parser.add_argument("--course", help="enter the course you want")
    args = parser.parse_args()
    norm = 0
    course = "all"
    if args.norm and args.norm == "true":
        norm = 1
        print(args.norm)
    if args.course:
        course = args.course
    histogram(norm, course)
