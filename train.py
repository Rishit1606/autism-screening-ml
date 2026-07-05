import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import pickle

df = pd.read_csv('data/autism_screening.csv')
df = df.drop(columns =['age_desc','result'])

# replaces all values where conditions are not met with NaN
df['age'] = df['age'].where(df['age'] <= 100)

# filling NaN with median age
df['age'] = df['age'].fillna(df['age'].median())



print(df['age'].describe())
print(df.shape)
print(df.isnull().sum())

# Shows how many YES vs NO in our target column
print(df['Class/ASD'].value_counts())