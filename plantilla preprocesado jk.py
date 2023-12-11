"""
Created on Wed Dec  6 22:24:07 2023

@author: joaco
"""

#plantilla preprocesado:
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


#3. División datos en set Training y set Testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=0)

print(x_train)
print(x_test)
print(y_train) 
print(y_test) 

"""#4. Escalado de datos
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train =sc_x.fit_transform(x_train)
x_test= sc_x.transform(x_test)

# No hace falta hacerlo para y -> algoritmo de categorizacion."""