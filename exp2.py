#Exp 02: Inferential statitics
import pandas as pf
import numpy as np
import math
df = pd.read_csv("facebook.csv")
df.info()
df.isnull().sum()
df.shape

sample = df["age"][np.argsort(np.random.rand(47))[:30]]
smean = sample.mean()
mean = df["age"].mean()
print(mean)
N=47
std = df["age"].std()
z = (smean-mean)/std/math.sqrt(N)
if(z>1.96):
    print("Value is rejected")
else:
    print("Value is accepted")
