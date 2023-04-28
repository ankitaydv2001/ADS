#Exp 5:

import pandas as pd
import numpy as np
from matplotlib.pyplot import *
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import *

df = read_csv('airports.csv')
df=df.dropna()
x = DataFrame(df['lat'])
y = DataFrame(df['long'])

x1, x2, y1, y2 = split(x, y, test_size=0.2)
model= LinearRegression().fit(x1, y1)
yp = model.predict(x2)

scatter(y2,yp)

print('MAE:', mean_absolute_error(y2, yp))
print('RMSE:', np.sqrt(mean_squared_error(y2, yp))) 
print('MAPE:', mean_absolute_percentage_error(y2, yp))

