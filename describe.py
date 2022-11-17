# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import sys
import lib_math as lb 
import operation_data 
from histogram import histogram 

def describe():

    # file_name = str(sys.argv[1])
    # try:
    #     data_train = pd.read_csv(file_name)
    # except FileNotFoundError:
    #     print("The file you entre can't be read")
    #     exit()

    data_train = pd.read_csv("./datasets/dataset_train.csv")

    #Recuperation des colonnes a valeur numeriques
    numeric_data = data_train.select_dtypes(include='number')
    
    #Suppression des colonnes non pertinentes
    numeric_data = numeric_data.drop('Index', axis = 1)

    numeric_data = numeric_data.dropna()
    
    #Recuperation des noms des features
    list_features = numeric_data.columns
    
    #Initialisation de la liste des informations 
    specifics = []

    for feature in numeric_data:
        #Pour chaque feature, on ajoute a la liste un tuple de la forme
        #(count,mean,std,min,25,50,75,max)
        specifics.append((lb.ft_count(data_train[feature]),
                          lb.ft_mean(data_train[feature]),
                          lb.ft_std(data_train[feature]),
                          lb.ft_min(data_train[feature]),
                          lb.first_quartile(data_train[feature]),
                          lb.median(data_train[feature]),
                          lb.third_quartile(data_train[feature]),
                          lb.ft_max(data_train[feature]),
                          )
                         )
        
    specs = pd.DataFrame(data=specifics,
                         index=list_features,
                         columns=['Count', 'Mean','Std', 'Min', '25 %', '50 %', '75 %', 'Max']).T
    
    print(specs)
    
   
if __name__ == "__main__":
    describe()

