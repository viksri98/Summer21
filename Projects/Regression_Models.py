#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:04:24 2021

@author: vikram
"""
<<<<<<< HEAD
#%% import usual necessities, plus new linear regression
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#%% import linear modeling from scikitlearn
from sklearn import linear_model as lm
#%% bring in and convert the daylight data
daylight_data = pd.read_csv('../src/DaylightScatterPlot.csv')
latitude = daylight_data['Latitude']
daylight_hours = daylight_data['Number of Daylight Hours']
#%% plot
plt.scatter(latitude_ints, daylight_hours)
#%% Linear Regression
model = lm.LinearRegression()
model.fit(latitude_ints.reshape(-1, 1), daylight_hours)
x = np.linspace(0, 70, 100)
y= model.predict(x.reshape(-1, 1))
plt.scatter(latitude_ints, daylight_hours)
plt.plot(x, y)
plt.xlabel("latitude (degrees north)")
plt.ylabel("daylight hours")
plt.show()
#%% get slope and intercept
slope = model.coef_
intercept = model.intercept_
=======
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
>>>>>>> 0a0fb492bb7e4b09f007072472c961f43a3f5125
