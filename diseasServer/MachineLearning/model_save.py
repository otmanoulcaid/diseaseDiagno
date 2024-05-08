
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# models = {
#     'DecisionTreeClassifier' : DecisionTreeClassifier(criterion='entropy', max_depth=16, min_samples_split=6),
#     'LogisticRegression' : LogisticRegression(C=0.1, max_iter=200, penalty='l2', solver='liblinear'),
#     'KNN' : KNeighborsClassifier(algorithm = 'ball_tree', leaf_size = 20, n_neighbors = 3, weights = 'uniform')
# }


df = pd.read_csv("DataSet.csv")
labelEnc = LabelEncoder()
df['prognosis'] = labelEnc.fit_transform(df['prognosis'])
feats = df.iloc[:, :-1] 
labels = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(feats, labels, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(algorithm = 'ball_tree', leaf_size = 20, n_neighbors = 5, weights = 'uniform')
lr = LogisticRegression(C=0.1, max_iter=200, penalty='l2', solver='newton-cg')
dt = DecisionTreeClassifier(criterion='entropy', min_samples_split=6)

knn.fit(X_train, y_train)
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Save the model to a file using Joblib
joblib.dump(knn, 'DecisionTree.pkl')
joblib.dump(knn, 'knn.pkl')
joblib.dump(knn, 'LogesticRegression.pkl')


# # statistic = Statistic(feats, labels)
# # result = statistic.models_metrics(models)
# # print(pd.DataFrame(result))

# knn = joblib.Load("knn.pkl")
# pedicr = knn.predict(X_test)
