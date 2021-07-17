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
#%% bring in the punting data
punting_data = pd.read_csv('~/Documents/Summer21/src/punting_data.txt')
distance = punting_data['Distance']
kick_leg = punting_data['R_Strength']
plant_leg = punting_data['L_Strength']
#%% plot
plt.scatter(kick_leg, distance)
#%% Lets make trendlines