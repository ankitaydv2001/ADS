#Exp 01:

import pandas as pd
df = pd.read_excel("rtrial.xlsx")
df.shape
df.info()
df["x"].mean()
df["x"].median()
df["x"].mode()

df["x"].skew()
df["x"].kurt()
df["x"].max()
df["x"].min()

print(df["x"].max()-df["x"].min())

df["x"].std()
df["x"].var()
