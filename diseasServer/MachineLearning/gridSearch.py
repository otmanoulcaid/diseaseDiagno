from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from preprocessing import Encoder
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# Define grid search function
def gridSearchCV(estimator, param_grid, X, y, scoring):
    g_s = GridSearchCV(estimator, param_grid, cv=5, scoring=scoring, n_jobs=-1)
    g_s.fit(X, y)
    return g_s.best_estimator_, g_s.best_params_

# Load dataset
df = pd.read_csv("../DataSet.csv")

# Encode labels
Enc = Encoder()
df['prognosis'] = Enc.fit_transform(df['prognosis'])

# Split dataset into training and testing sets
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

# Prepare features and labels
feats = df_train.iloc[:, :-1]
label = df_train.iloc[:, -1]

# Initialize KNN classifier
knn = KNeighborsClassifier()

# Define hyperparameter grid for KNN
param_knn = {
    'n_neighbors': [3, 1, 5],
    'leaf_size': [20, 10],
    'weights': ['uniform', 'distance'],
    'algorithm' : [ 'ball_tree', 'kd_tree']
}

# Perform grid search
best_estimator, best_params = gridSearchCV(knn, param_knn, feats, label, scoring="accuracy")

# Print best estimator and best parameters
print("Best estimator:", best_estimator)
print("Best parameters:", best_params)


# # decision tree
# d_t = DecisionTreeClassifier()
# param_grid = {
#     "criterion" : ["gini", "entropy", "log_loss"],
#     "splitter" : ["best", "random"],
#     "max_depth" : [8, 12, 16],
#     "min_samples_split" : [2, 6, 10],
# }
# D_T_best_estimator, best_params, best_score = gridSearchCV(feats, label, estimator = d_t, param_grid=param_tree, scoring='accuracy') #f1_macro
# print (D_T_best_estimator)
# print (best_params)
# print (best_score)

# # LogisticRegression
# l_r = LogisticRegression()
# param_grid = {
#     'penalty' : ['l1', 'l2'],
#     'solver'  : ['liblinear'],
#     'C': [0.1, 1, 10],
#     'max_iter': [200, 500],
# }
# L_R_best_estimator, best_params, best_score = gridSearchCV(feats, label, estimator = l_r, param_grid=param_l_r, scoring="accuracy") #f1_macro
# print (L_R_best_estimator)
# print (best_params)
# print (best_score)



# from sklearn.metrics import accuracy_score
# feats_test = df_train.iloc[:,:-1]
# label_test = df_train.iloc[:,-1]
# #----------------------------------
# print("accuracy on test data of decision tree model")
# D_T_best_estimator.fit(feats, label)
# valid_l_pred = D_T_best_estimator.predict(feats_test)
# print(accuracy_score(valid_l_pred, label_test))
# #----------------------------------
# print("accuracy on test data of logistic regression model")
# L_R_best_estimator.fit(feats, label)
# valid_l_pred = L_R_best_estimator.predict(feats_test)
# print(accuracy_score(valid_l_pred, label_test))

