#Exp 04:
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("facebook.csv")

#Histogram
plt.hist(df["age"])
plt.show()

#Quartile
plt.boxplot(df["dob_year"])
plt.show()

#Distribution chart
sns.distplot(df["age"])
plt.show()

#Scatterplot
plt.scatter(df["age"], df["dob_year"])
plt.show()

#ScatterMultiple
plt.scatter(df["age"], df["dob_year"])
plt.scatter(df["dob_day"], df["tenure"])
plt.show()

#Scatter Matrix
import plotly.express as pl
pl.scatter_matrix(df)

#Bubble Chart
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)
plt.scatter(x,y,z*1000)
plt.show()

#Density chart
df["age"].plot.density()

#Parrallehart
import plotly.express as pl
dim = ['userid', 'age']
pl.parallel_coordinates(df, dimensions=dim).show()

#Deviation graph
data=df["age"]
df=pd.DataFrame({"x":data, 
              'y':[i for i in range(len(data))], 
              'z':[i for i in range(len(data))]})
df.plot()
plt.show()
