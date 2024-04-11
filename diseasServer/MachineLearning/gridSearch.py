from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from transformer import Encoder
import pandas as pd

# from sklearn.multiclass import OneVsRestClassifier

def gridSearchCV(*args, **kwargs):
    g_s = GridSearchCV(kwargs["estimator"], kwargs["param_grid"], cv=5, scoring=kwargs["scoring"], return_train_score=True)
    g_s.fit(args[0], args[1])
    return (g_s.best_estimator_, g_s.best_params_)



df = pd.read_csv("DataSet.csv")
Enc = Encoder()
feats = df.iloc[:,:-1]
labels = df.iloc[:,-1]
label = Enc.fit_transform(labels)

# decision tree

d_t = DecisionTreeClassifier()
param_tree = {
    "criterion" : ["gini", "entropy", "log_loss"],
    "splitter" : ["best", "random"],
    "max_depth" : [8, 12, 16],
    "min_samples_split" : [2, 6, 10],
}
best_estimator, best_params = gridSearchCV(feats, label, estimator=d_t, param_grid=param_tree, scoring='accuracy') #f1_macro
print (best_estimator)
print (best_params)

# # KNN

knn = KNeighborsClassifier()
param_knn = {
    'n_neighbors'   : [3, 5, 7],
    'leaf_size'     : [20, 30, 40],
    'weights'       : ['uniform', 'distance'],
}
best_estimator, best_params = gridSearchCV(feats, label, estimator=knn, param_grid=param_knn, scoring="accuracy") #f1_macro
print (best_estimator)
print (best_params)

# LogisticRegression

l_r = LogisticRegression()
param_l_r = {
    'penalty' : ['l1', 'l2'],
    'solver'  : ['liblinear'],
    'C': [0.1, 1, 10],
    'max_iter': [200, 500],
}
best_estimator, best_params = gridSearchCV(feats, label, estimator=l_r, param_grid=param_l_r, scoring="accuracy") #f1_macro
print (best_estimator)
print (best_params)