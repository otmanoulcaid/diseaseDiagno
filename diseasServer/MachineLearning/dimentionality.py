from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from sklearn.decomposition import PCA
import pandas as pd

#sklearn algorithms used in our projects
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier



def reduction(**kwargs):
    X_train, X_test, y_train, y_test = train_test_split(kwargs['feats'], kwargs['labels'], test_size=0.3, random_state=42)
    pca = PCA(n_components=41)
    X_train_reduced = pca.fit_transform(X_train)
    X_test_reduced = pca.transform(X_test)
    kwargs["model"].fit(X_train_reduced, y_train)
    y_pred_reduced = kwargs["model"].predict(X_test_reduced)
    return (accuracy_score(y_test, y_pred_reduced), f1_score(y_test, y_pred_reduced, average='macro'))

df = pd.read_csv("DataSet.csv")
labelEnc = LabelEncoder()
df['prognosis'] = labelEnc.fit_transform(df['prognosis'])
feats = df.iloc[:, :-1] 
labels = df.iloc[:, -1]

# Train a LogisticRegression model on the reduced data
model = LogisticRegression(C=0.1, max_iter=200, penalty='l2', solver='liblinear')
accuracy_reduced, f1 = reduction(model=OneVsRestClassifier(model), feats=feats, labels=labels)
print("Accuracy on reduced data of LogisticRegression:", accuracy_reduced, f1)

# Train a KNeighborsClassifier model on the reduced data
model = KNeighborsClassifier(leaf_size=20, n_neighbors=3)
accuracy_reduced, f1 = reduction(model=OneVsRestClassifier(model), feats=feats, labels=labels)
print("Accuracy on reduced data of KNeighborsClassifier:", accuracy_reduced, f1)

# Train a DecisionTreeClassifier model on the reduced data
model = DecisionTreeClassifier(criterion='entropy', max_depth=16, min_samples_split=6)
accuracy_reduced, f1 = reduction(model=OneVsRestClassifier(model), feats=feats, labels=labels)
print("Accuracy on reduced data of DecisionTreeClassifier:", accuracy_reduced, f1)

