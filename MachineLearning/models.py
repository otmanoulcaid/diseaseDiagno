import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# custom classes

class   Operations():
    def Operations(self):
        return (self)

    def fitPredict(slf, model, train_feat, train_label, test_feat):
        model.fit(train_feat, train_label)
        return (model.predict(test_feat))

    def accuracy(self, encoded_label, predict_label):
        return (accuracy_score(encoded_label, predict_label))


class   Statistic(Operations):
    def __init__(self, df_train, df_test):
        self.df_train = df_train
        self.df_test = df_test
    
    # method calculate the the accuracy_of multiple models given dictionary of algorithms and piplines
    # and return a list of accuracy statistic 
    def models_accuracy(self, classification_models ,feature_prepros, label_prepros):
        result = []
        for model_name, model in classification_models.items():

            #training and testing data preprocessed
            test_f  = feature_prepros.fit_transform(self.df_test)
            test_l  = label_prepros.fit_transform(self.df_test)
            train_f = feature_prepros.fit_transform(self.df_train)
            train_l = label_prepros.fit_transform(self.df_train)

            # Fit the model on the training data
            # Predict on both training and validation sets
            train_l_pred = self.fitPredict(model, train_f, train_l, train_f)
            valid_l_pred = self.fitPredict(model, train_f, train_l, test_f)

            # Saving the results in the list
            result.append({
                'Model': model_name,
                'Training Accuracy': self.accuracy(train_l, train_l_pred),
                'Validation Accuracy': self.accuracy(test_l, valid_l_pred)
                })
        return pd.DataFrame(result)