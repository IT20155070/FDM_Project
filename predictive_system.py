# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 02:30:20 2022

@author: sadini
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (0,1,3,0,2,2,0,2,3,1)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('Resort Hotel')
else:
  print('City Hotel')