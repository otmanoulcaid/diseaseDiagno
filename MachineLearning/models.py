import pandas as pd
from sklearn.preprocessing import LabelEncoder

#some of sklearn algorithms used in our projects

from sklearn.svm import SVC
from IPython.display import display
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
