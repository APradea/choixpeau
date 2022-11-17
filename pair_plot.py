#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Mon Nov  7 15:14:01 2022@author: anthelme"""import pandas as pdimport numpy as npimport sysimport lib_math as lbimport operation_dataimport argparseimport matplotlib.pyplot as pltfrom histogram import create_histogram from scatterplot import create_scatter def pair_plot():    df = pd.read_csv("./datasets/dataset_train.csv", index_col = "Hogwarts House").select_dtypes("number")    df = df.drop('Index', axis = 1)    df = df.dropna()        list_features = df.columns            lf_len = lb.ft_count(list_features)    fig, axs = plt.subplots(lf_len, lf_len, figsize=(16,7))        x = 0    y = 0        for feature_y in list_features:        x = 0        for feature_x in list_features:            if feature_x == feature_y:                create_histogram(df, feature_x, axs[y,x])            else:                create_scatter(df, feature_x, feature_y, axs[y,x])            axs[y,x].set_xlabel(feature_x)            axs[y,x].set_ylabel(feature_y)            axs[y,x].label_outer()            x = x + 1        y = y + 1            fig.legend(['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])    plt.show()if __name__ == "__main__":    pair_plot()