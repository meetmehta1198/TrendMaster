#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:35:10 2020

@author: meetmehta
"""


import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split


df=pd.read_csv('/Users/meetmehta/Desktop/Web_Scrapping/trending_final.csv',header=0)


X=df.iloc[:,0:11]
Y=df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X, Y,test_size=0.3)

model = Sequential()
model.add(Dense(6,input_dim=11,activation='relu'))
model.add(Dense(5,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])


model.fit(X_train,y_train,epochs=100,batch_size=16)
_,accuracy = model.evaluate(X_test,y_test)

print("Accuracy : %.2f"%(accuracy*100))
