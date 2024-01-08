import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

datasets_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'diabetes.csv')
df = pd.read_csv(datasets_path)

X = df.drop(['Outcome', 'DiabetesPedigreeFunction'],axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.svm import SVC

model_svm = SVC(probability=True,random_state=42)
model_svm.fit(X_train, y_train)
y_pred = model_svm.predict(X_test)

def predict_diabetes(attributes):
    input_data = np.array(attributes).reshape(1, -1)
    probability_diabetes = model_svm.predict_proba(input_data)[:, 1]
    return probability_diabetes[0]


