# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:56:59 2023

@author: joaco
"""

###PLANTILLA DE PREPROCESADO - DATOS CATEGORICOS###

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

#3. codificar datos categoricos -> paises a numeros por ej.

from sklearn.preprocessing import LabelEncoder

#creo codificador de datos
labelencoder_x = LabelEncoder()

#transformo datos:
labelencoder_x.fit_transform(x[:,0])
print(labelencoder_x.fit_transform(x[:,0]))

#modifico columna de data set con los nuevos datos modificados:
    
x[:,0]= labelencoder_x.fit_transform(x[:,0])

print(x) #listo

#hay un problema! quedan variables ordinales (con orden) 
#entonces usamos variables dummy: vectores de formato (x,y,z,...,n) segun el n de observaciones a completar
#para esto, utilizamos de vuelta sklearn

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'),[0])], remainder='passthrough')

    
x=np.array(ct.fit_transform(x), dtype=np.float64)


#Para variable y:
    
labelencoder_y = LabelEncoder()
labelencoder_y.fit_transform(y)
y=labelencoder_y.fit_transform(y)
print(y)
