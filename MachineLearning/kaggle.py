import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from IPython.display import display


#some of sklearn algorithms used in our projects

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier


#read training csv using read_scv method that convert the csv content to a dataframe
df=pd.read_csv("Training.csv")
# print(df)


df_test=pd.read_csv("Testing.csv")
# print(df_test)


# clean the data by dropping the null or empty feature (column)
df = df.drop(columns=['Unnamed: 133'])
#print(df.head)


#assigning the all the rows (:) of all the columns of our dataFrame execpt the last one (:-1) to X
#so in X we have all the features
#and the all the rows of the last column (-1) so that we have in Y all the labels
X, y=df.iloc[:,:-1], df.iloc[ :,-1]
#print(X,y)

X_test, y_test=df_test.iloc[19:20,:-1], df_test.iloc[ 19:20,-1]
#print(X_test,y_test)

#instanciate an object from LabelEncoder() class in order to encode all the labels using integer encoding
#look at the ML Notes File (wrotten by otman oulcaid)
label_encoder_y = LabelEncoder()

# Fit and transform y of tain dataframe
y_encoded = label_encoder_y.fit_transform(y)
# print(y_encoded)

# Fit and transform y of test dataframe
y_testencoded = label_encoder_y.fit_transform(y_test)
# print(y_testencoded)



#creating a dictionary that contains all the algorithms that we will deal with 

classification_models = {
    'Logistic Regression': LogisticRegression(),
    # 'Decision Tree': DecisionTreeClassifier(),
    # 'Random Forest': RandomForestClassifier(n_jobs=-1, random_state=666),
    # 'Gradient Boosting': GradientBoostingClassifier(),
    # 'SVM': SVC(),
    # 'K-Nearest Neighbors': KNeighborsClassifier(),
    # 'Naive Bayes': GaussianNB(),
    # 'Neural Network': MLPClassifier()
}

#loop through all the the algorithms and save the result into an array list of dictionary
result_list=[]

for model_name, model in classification_models.items():
        # Fit the model on the training data
        model.fit(X, y_encoded)

        # Predict on both training and validation sets
        y_train_pred = model.predict(X)
        y_valid_pred = model.predict(X_test)
        print(X_test)
        print(y_valid_pred)

        # Calculate accuracy scores
        train_accuracy = accuracy_score(y_encoded, y_train_pred)
        valid_accuracy = accuracy_score(y_testencoded, y_valid_pred)
        
        

        # Save the results in the list
        result_list.append({
            'Model': model_name,
            'Training Accuracy': train_accuracy,
            'Validation Accuracy': valid_accuracy})


# Convert the list of dictionaries into a DataFrame
result_df = pd.DataFrame(result_list)

display(result_df)
