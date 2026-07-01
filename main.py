import pandas as pd
df = pd.read_csv('data/autism_screening.csv')
print(df.shape)
print(df.columns.tolist())
print(df.head())