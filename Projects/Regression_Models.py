#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:04:24 2021

@author: vikram
"""
#%% import usual necessities
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
#%% bring in the punting data
punting_data = pd.read_csv('~/Downloads/puntingdata2.txt')
distance = punting_data['Distance']
kick_leg = punting_data['R_Strength']
plant_leg = punting_data['L_Strength']
#%% plot
plt.scatter(kick_leg, distance)
#%% Linear regression,
plt.scatter(kick_leg, distance)
lin = stats.linregress(kick_leg, distance)
plt.plot(kick_leg, lin.slope * kick_leg + lin.intercept)
plt.title('kick leg v distance')
print(lin.rvalue)
#%% do the same for plant_leg and distance
plt.scatter(plant_leg, distance)
lin = stats.linregress(plant_leg, distance)
plt.plot(plant_leg, lin.slope * plant_leg + lin.intercept)
plt.title('plant leg v distance')
print(lin.rvalue)
#%%
plt.scatter(plant_leg + kick_leg, distance)
lin = stats.linregress(plant_leg + kick_leg, distance)
plt.plot(plant_leg + kick_leg, lin.slope * (plant_leg + kick_leg) + lin.intercept)
plt.title('legs v distance')
print(lin.rvalue)