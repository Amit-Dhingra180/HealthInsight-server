
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

datasets_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'heart.csv')
df = pd.read_csv(datasets_path)


X = df.drop('target', axis=1)
y = df['target']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


rf_model = RandomForestClassifier()


rf_model.fit(X_train, y_train)

def predict_heart(attributes):
    input_data = np.array(attributes).reshape(1, -1)
    probability = rf_model.predict_proba(input_data)[:, 1]
    return probability[0]
