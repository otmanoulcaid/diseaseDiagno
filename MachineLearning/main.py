from preprocessing import FeatureGetter, LabelGetter, Encoder, Droper, DataExtractor
from models import Statistic
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

models = {
    'DecisionTreeClassifier' : DecisionTreeClassifier(criterion='entropy', max_depth=16, min_samples_split=6),
    'KNeighborsClassifier' : KNeighborsClassifier(leaf_size=20, n_neighbors=3),
    'LogisticRegression' : LogisticRegression(C=0.1, max_iter=200, penalty='l2', solver='liblinear')
}

df = pd.read_csv("DataSet.csv")
labelEnc = LabelEncoder()
df['prognosis'] = labelEnc.fit_transform(df['prognosis'])
feats = df.iloc[:, :-1] 
labels = df.iloc[:, -1]

statistic = Statistic(feats, labels)

result = statistic.models_metrics(models)

print(pd.DataFrame(result))