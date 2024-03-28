from preprocessing import FeatureGetter, LabelGetter, Encoder, Droper, DataSpliter
from sklearn.pipeline import Pipeline
from models import Statistic
import pandas as pd

#some of sklearn algorithms used in our projects

from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
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
            "KNeighborsClassifier" : KNeighborsClassifier(n_neighbors=3),
            "MLPClassifier" : MLPClassifier()
        }
        
statistic = Statistic(df_train, df_test)
accuracy = statistic.models_accuracy(models, feature_prepros, label_prepros)
print(accuracy)

# spliter = DataSpliter(0.5, 4)
# X_train, X_test, y_train, y_test = spliter.split(train_feat, train_label)


# test_feat = feature_prepros.fit_transform(df_test)
# test_label = label_prepros.fit_transform(df_test)
# train_feat = feature_prepros.fit_transform(df_train)
# train_label = label_prepros.fit_transform(df_train)


# print(df_test['prognosis'].tolist())
# features = test_feat.columns

# model_name = mod.algos["LogisticRegression"]
# train_predect = mod.predict_label( model_name, train_feat, train_label, train_feat)
# test_predect = mod.predict_label( model_name, train_feat, train_label, test_feat)
# train_accuracy = mod.accuracy(train_label, train_predect)
# valid_accuracy = mod.accuracy(test_label, test_predect)

# print(train_accuracy)
# print(valid_accuracy)