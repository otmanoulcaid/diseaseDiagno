from preprocessing import FeatureGetter, LabelGetter, Encoder, Droper, DataSpliter
from sklearn.pipeline import Pipeline
from models import Statistic
import pandas as pd

#some of sklearn algorithms used in our projects

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#read training csv using read_scv method that convert the csv content to a dataframe
df_train=pd.read_csv("Training.csv")
# print(df)

df_test=pd.read_csv("Testing.csv")
# print(df_test)

feature_prepros = Pipeline([
    ("drop", Droper()),
    ("f_getter", FeatureGetter())
])

label_prepros = Pipeline([
    ("drop", Droper()),
    ("get_l", LabelGetter()),
    ("label_encoder", Encoder())
])

#tests of pipelines

models = {
            "LogisticRegression" : LogisticRegression(),
            "DecisionTreeClassifier" : DecisionTreeClassifier(),
            "RandomForestClassifier" : RandomForestClassifier(n_estimators=100), 
        }
        
statistic = Statistic(df_train, df_test)
accuracy = statistic.models_accuracy(models, feature_prepros, label_prepros)
print(accuracy)
