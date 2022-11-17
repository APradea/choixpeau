#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:14:01 2022

@author: anthelme
"""

import numpy as np
import pandas as pd
import operation_data as od
import csv
import sys
from lib_math import ft_count


SELECTED_FEATURES = ["Defense Against the Dark Arts","Divination","Charms", "History of Magic", "Ancient Runes", 'Flying']

class LogRegPredict():
    
    def __init__(self, df, theta):
        self.df = df
        self.X = np.insert(np.array(df), 0, np.ones(len(df)), axis=1)
        self.theta = theta

        self.scores = []
        self.prediction = []
        
    def sigmoid(self, X):
        return 1 / (1 + np.exp(-X))

        self.prediction = []
        
    def sigmoid(self, X):
        return 1/(1 + np.exp(-X))
    
    def predict(self):
        for x in self.X:
            score = {}
            for house in self.theta.columns:
                teta_house = np.array(self.theta[house])
                # le produit matriciel renvoi une une unique valeur
                # la probabilité qu'un eleve aille dans une maison
                score[house] = self.sigmoid(np.dot(x, teta_house))
                self.scores.append(score)
                score[house]=self.sigmoid(np.dot(x, np.array(self.theta[house])))
            self.prediction.append(score)
    
    def output(self):
        filename = './prediction.csv'
        f = open(filename, 'w+')
        w = csv.writer(f)
        w.writerow(['Index', 'Hogwarts House'])

        # pour choisir dans quel maison va l'eleve on prend le score le plus elevé
        for i in range(ft_count(self.scores)):
            row = [i, max(self.scores[i], key=self.scores[i].get)]
            self.prediction.append(row)
            w.writerow(row)

        for i in range(len(self.prediction)):
            row = [i, max(self.prediction[i], key=self.prediction[i].get)]
            w.writerow(row)
            

    
        
def get_theta():
    try:
        return pd.read_csv('./theta.csv')
    except :
        raise Exception("File not found or error while opening")

def logreg_predict(file):
    try:
        data_test = pd.read_csv(file)
    except:
        raise Exception("File not found or error while opening the file")
       
    # on recupere les features qui nous interessent
    df =  data_test[SELECTED_FEATURES]
    
    # on recupere les infos de logreg_train
    theta = get_theta()
    
    # on norme les valeurs du df 
    std = od.norm_values(df)
    
    # on met des zeros à la place des valeurs manquantes, revient a mettre la 
    # moyenne
    new_df = od.replace_missing_values_by_zeros(std)
    
    # on initialise la classe
    logredpred = LogRegPredict(new_df, theta)
    

    logredpred.predict()
    
    logredpred.output()
        
    # from sklearn.metrics import accuracy_score
    # P = pd.read_csv('prediction.csv')
    # P = P['Hogwarts House']
    # print(accuracy_score(y_train, P))

if __name__ == "__main__" :
    if __name__ == "__main__":
        if ft_count(sys.argv) > 1:
            logreg_predict(sys.argv[1])
        else:
            print("put a file plz")

        
theta = get_theta()
        
data_test = pd.read_csv("./datasets/dataset_test.csv")
   
dff =  data_test[SELECTED_FEATURES]
std = od.norm_values(dff)
new_df = od.replace_missing_values_by_zeros(std)
A = LogRegPredict(new_df, theta)
A.predict()
A.output()
X = A.X






