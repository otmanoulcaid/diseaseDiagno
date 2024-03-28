import pandas as pd
from sklearn.preprocessing import LabelEncoder

#some of sklearn algorithms used in our projects

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# custom classes

class   Operations():
    def Operations(self):
        return (self)

    def predict_label(slf, model, train_feat, train_label, test_feat):
        model.fit(train_feat, train_label)
        return model.predict(test_feat)

    def accuracy(self, encoded_label, predict_label):
        return accuracy_score(encoded_label, predict_label)

class   Models(Operations):

    def Models(self):
        return (self)

    algos = {
                "LogisticRegression" : LogisticRegression(),
                "DecisionTreeClassifier" : DecisionTreeClassifier(),
                "RandomForestClassifier" : RandomForestClassifier(), 
                "GradientBoostingClassifier" : GradientBoostingClassifier(),
                "SVC" : SVC(), 
                "KNeighborsClassifier" : KNeighborsClassifier() ,
                "GaussianNB" : GaussianNB(),
                "MLPClassifier" : MLPClassifier()
            }

