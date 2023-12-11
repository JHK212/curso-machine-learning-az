# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:58:10 2023

@author: joaco
"""
###PLANTILLA DE PREPROCESADO - DATOS FALTANTES###

#1. importacion de librerias y dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("Data.csv")

#2. Separacion variable dependiente e independiente ->> En R no hace falta
x=dataset.iloc[:, :-1].values
y=dataset.iloc[:,3].values
print(x)
print(y)

#3. Limpieza de NAs-> Los vamos a promediar con otros datos similares
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)