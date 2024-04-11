from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.decomposition import PCA
import pandas as pd

# custom classes

class   Metrics():
    def Metrics(self):
        return (self)
    def accuracy(self, encoded_label, predict_label):
        return (accuracy_score(encoded_label, predict_label))
    def recall(self, encoded_label, predict_label):
        return recall_score(encoded_label, predict_label, average='macro')
    def f1Score(self, encoded_label, predict_label):
        return f1_score(encoded_label, predict_label, average='macro')
    def precision(self, encoded_label, predict_label):
        return precision_score(encoded_label, predict_label, average='macro')

class   Statistic(Metrics):
    def __init__(self, df_feat, df_label):
        self.df_feat = df_feat
        self.df_label= df_label
    
    def reduction(self, model, *args):
        pca = PCA(n_components=41)
        X_train_reduced = pca.fit_transform(args[0])
        X_test_reduced = pca.transform(args[1])
        model.fit(X_train_reduced, args[2])
        return (model.predict(X_test_reduced))


    # and return a list of metrics statistic 
    def models_metrics(self, classification_models):
        result = []
        train_f, test_f, train_l, test_l = train_test_split(self.df_feat, self.df_label, test_size=0.2, random_state=42)
        for model_name, model in classification_models.items():
            # fit and Predict on both training and validation sets
            model.fit(train_f, train_l)
            valid_l_pred = model.predict(test_f)
            valid_l_pred_reduced = self.reduction(model, train_f, test_f, train_l)
            # Saving the results in the list
            result.append({
                'Model': model_name,
                'f1score' : self.f1Score(test_l, valid_l_pred),
                'f1score reduced' : self.f1Score(test_l, valid_l_pred_reduced),
                'recall' : self.recall(test_l, valid_l_pred),
                'recall reduced' : self.recall(test_l, valid_l_pred_reduced),
                'precision' : self.precision(test_l, valid_l_pred),
                'precision reduced' : self.precision(test_l, valid_l_pred_reduced),
                'Accuracy': self.accuracy(test_l, valid_l_pred),
                'Accuracy reduced': self.accuracy(test_l, valid_l_pred_reduced)
                })
        return (result)


    