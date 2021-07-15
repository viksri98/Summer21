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
candy_data = pd.read_csv('~/Documents/Python/Summer21/src/candy_data.csv')

#%% examine the dataframe
print(candy_data.keys())
candy_names = candy_data['competitorname']
win_percent = candy_data['winpercent']
# Get the sugarpercent data into a new variable below
sugar_percent = candy_data['sugarpercent']
#%% Lets try using numpy with pandas dataframes
# Does it work well?
win_percent_np = np.array(win_percent)
mean_win = np.mean(win_percent)
mean_win_np = np.mean(win_percent_np)

#%% it does not work well with matplotlib, you should convert to numpy arrays first
# convert your sugarpercent dataframe to a numpy array
# use matplotlib to plot a graph of winpercent vs sugarpercent

sugar_np = np.array(sugar_percent)
plt.scatter(sugar_np, win_percent_np)
plt.title("Win Percent vs Sugar Percent")
plt.xlabel("Sugar Percent")
plt.ylabel("Win Percent")
plt.grid()
#%% price vs win
price_percent = np.array(candy_data['pricepercent'])
plt.scatter(price_percent, win_percent_np)
plt.title("wins vs price")
plt.xlabel("price")
plt.ylabel("win percent")
plt.grid()