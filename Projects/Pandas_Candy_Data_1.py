#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 20:42:09 2021

@author: vikram
"""

#%%  import useful modules
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#%%import a dataframe
candy_data = pd.read_csv('../src/candy_data.csv')

#%% examine the dataframe
print(candy_data.keys())
candy_names = candy_data['competitorname']
win_percent = candy_data['winpercent']
# Get the sugarpercent data into a new variable below

#%% Lets try using numpy with pandas dataframes
# Does it work well?
win_percent_np = np.array(win_percent)
mean_win = np.mean(win_percent)
mean_win_np = np.mean(win_percent_np)

#%% it does not work well with matplotlib, you should convert to numpy arrays first
# convert your sugarpercent dataframe to a numpy array
# use matplotlib to plot a graph of winpercent vs sugarpercent

