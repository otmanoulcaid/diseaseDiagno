from preprocessing import FeatureGetter, LabelGetter, Encoder, Droper
from sklearn.pipeline import Pipeline
from models import Models
import pandas as pd

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

test_feat = feature_prepros.fit_transform(df_test)
test_label = label_prepros.fit_transform(df_test)
train_feat = feature_prepros.fit_transform(df_train)
train_label = label_prepros.fit_transform(df_train)

print(train_feat)
#test algos

# mod = Models()
# model_name = mod.algos["LogisticRegression"]
# train_predect = mod.predict_label( model_name, train_feat, train_label, train_feat)
# test_predect = mod.predict_label( model_name, train_feat, train_label, test_feat)
# train_accuracy = mod.accuracy(train_label, train_predect)
# valid_accuracy = mod.accuracy(test_label, test_predect)

# print(train_accuracy)
# print(valid_accuracy)