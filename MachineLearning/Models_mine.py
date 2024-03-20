from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import pandas as pd


#some of sklearn algorithms used in our projects

# from sklearn.metrics import accuracy_score
# from IPython.display import display
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.neural_network import MLPClassifier

#read training csv using read_scv method that convert the csv content to a dataframe
df_train=pd.read_csv("Training.csv")
# print(df)

df_test=pd.read_csv("Testing.csv")
# print(df_test)

class FeatureGetter(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.iloc[:, :-1]
    
class LabelGetter(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.iloc[:, -1]  
     
class	Encoder(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        l_e = LabelEncoder()
        return l_e.fit_transform(X)

class   Droper(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
          return (self)
    def transform(self, X):
        if 'Unnamed: 133' in X.columns:
            return (X.drop(['Unnamed: 133'], axis=1))
        return X

#pipelines for features and encoded labels

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

print(feature_prepros.fit_transform(df_test))
print(label_prepros.fit_transform(df_test))

# #creating a dictionary that contains all the algorithms that we will deal with 

# classification_models = {
#     'Logistic Regression': LogisticRegression(),
#     # 'Decision Tree': DecisionTreeClassifier(),
#     # 'Random Forest': RandomForestClassifier(n_jobs=-1, random_state=666),
#     # 'Gradient Boosting': GradientBoostingClassifier(),
#     # 'SVM': SVC(),
#     # 'K-Nearest Neighbors': KNeighborsClassifier(),
#     # 'Naive Bayes': GaussianNB(),
#     # 'Neural Network': MLPClassifier()
# }

# #loop through all the the algorithms and save the result into an array list of dictionary
# result_list=[]

# for model_name, model in classification_models.items():
#         # Fit the model on the training data
#         model.fit(X, y_encoded)

#         # Predict on both training and validation sets
#         y_train_pred = model.predict(X)
#         y_valid_pred = model.predict(X_test)
#         print(X_test)
#         print(y_valid_pred)

#         # Calculate accuracy scores
#         train_accuracy = accuracy_score(y_encoded, y_train_pred)
#         valid_accuracy = accuracy_score(y_testencoded, y_valid_pred)
        
        

#         # Save the results in the list
#         result_list.append({
#             'Model': model_name,
#             'Training Accuracy': train_accuracy,
#             'Validation Accuracy': valid_accuracy})


# # Convert the list of dictionaries into a DataFrame
# result_df = pd.DataFrame(result_list)

# display(result_df)
