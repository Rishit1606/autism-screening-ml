import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import pickle

df = pd.read_csv('data/autism_screening.csv')

### Cleaning the data

# Removing unnecessary columns
df = df.drop(columns =['age_desc','result', 'contry_of_res'])

# replaces all values where conditions are not met with NaN
df['age'] = df['age'].where(df['age'] <= 100)

# filling NaN with median age
df['age'] = df['age'].fillna(df['age'].median())

df['ethnicity'] = df['ethnicity'].replace('?', 'Unknown')
df['relation'] = df['relation'].replace('?', 'Unknown')
df['ethnicity'] = df['ethnicity'].replace('others', 'Others')

#  Encoding non numerical values to make datatset trainable
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['jundice'] = le.fit_transform(df['jundice'])
df['austim'] = le.fit_transform(df['austim'])
df['used_app_before'] = le.fit_transform(df['used_app_before'])
df['Class/ASD'] = le.fit_transform(df['Class/ASD'])
df = pd.get_dummies(df, columns=['ethnicity', 'relation'])

### training the data

# splitting to features and target
X = df.drop(columns=['Class/ASD'])
y = df['Class/ASD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# training on RandomForest
rf = RandomForestClassifier(class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

# trianing on XGBoost
xgb = XGBClassifier(random_state=42, eval_metric='logloss')
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)

### saving model 

pickle.dump(xgb, open('model.pkl', 'wb'))
print("Model saved!")

### printing and checking results

# RandomForest results
print("Random Forest Results:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# XGBoost Results 
print("XGBoost Results:")
print(classification_report(y_test, y_pred_xgb))
print(f"Accuracy: {accuracy_score(y_test, y_pred_xgb)}")


# Shows how many YES vs NO in our target column
print(df['Class/ASD'].value_counts())



