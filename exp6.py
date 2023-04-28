from pandas import *
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split as split

df = read_csv('data.csv')

x = df['Role']
y = df['College']

x1, x2, y1, y2 = split(x, y, test_size=0.2)

print('Before', Counter(y1))
X, Y = SMOTE().fit_resample(x1, y1)
print('After', Counter(Y))
