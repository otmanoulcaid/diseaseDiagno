from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


class   DataSpliter():
    def __int__(self, size, random):
        self.t_size = size
        self.random_state = random
        return self

    def split(self, x, y)
        return (train_test_split(x, y, test_size=self.t_size, random_state=self.random_state))

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
