#Exp 03: Imputation methods
#1) CCA wala
import pandas as pd
df = pd.read_csv("facebook.csv")
df.isnull().sum()
df.dropna(axis=0)

#2) Random wala
df.isnull().sum()
df = df.fillna("Missing")

#3) Max wala value:
x = df["age"].mode()
print(x)
df = df.fillna(int(x))
print(df)
