from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import LabelEncoder

class   FeatureGetter(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.iloc[:, :-1]

class   LabelGetter(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.iloc[:, -1]  

class   Encoder(TransformerMixin, BaseEstimator):
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

class   DataExtractor():
    def DataExtractor(self):
        return self
    def symptoms(self, X):
        return(X.columns.tolist())
    def labels(self, X):
        return(X.prognosis.tolist())