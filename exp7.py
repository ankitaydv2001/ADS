# exp 07 (k_means wala):

from sklearn.cluster import KMeans
from pandas import *
from matplotlib.pyplot import *

df = read_csv('airports.csv')
x = df['lat']
y = df['long']
data = list(zip(x, y))
kmeans = KMeans(n_clusters=2).fit(data)
scatter(x, y, c=kmeans.labels_)
