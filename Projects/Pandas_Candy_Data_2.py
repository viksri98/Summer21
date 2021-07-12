#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:24:29 2021

@author: vikram
"""
#%%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#%% Lets mask the data so we only store the chocolate candies
candy_data = pd.read_csv('../src/candy_data.csv')
chocolates = candy_data[candy_data['chocolate'] == 1]
print(chocolates)
#%% Now plot sugarpercent vs winpercent for chocolates

#%% Plot sugarpercent vs winpercent for nougats