import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df_train = pd.read_csv("Training.csv")
df_test = pd.read_csv("Testing.csv")
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_train, df_test, test_size=0.4, random_state=42)

pipeline_selected = Pipeline([
    ('scaler', StandardScaler()),
    ('feature_selection', SelectKBest(score_func=f_classif, k=50)),
    ('pca', PCA(n_components=2)),
    ('clf', OneVsRestClassifier(LogisticRegression(max_iter=1000)))
])
