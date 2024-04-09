from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import pandas as pd


def parse_input(user_input):
    df = pd.read_csv("DataSet.csv")
    labelEnc = LabelEncoder()
    df['prognosis'] = labelEnc.fit_transform(df['prognosis'])
    X_train = df.iloc[: , :-1]
    y_train = df.iloc[:, -1]
    features = X_train.columns
    user_feat=[]
    for i in features:
        if i in user_input:
            user_feat.append(1)
        else:
            user_feat.append(0)
    return (X_train, y_train, user_feat)

def trained_model_prediction(input_feat):
    X_train, y_train, user_feat = parse_input(input_feat)
    user_feat_df = pd.DataFrame(columns=X_train.columns)
    user_feat_df.loc[0] = user_feat
    features = X_train.columns
    ##reduce dimentionality from 131 to 41
    # pca = PCA(n_components=41)
    # X_train_reduced = pca.fit_transform(X_train)
    # X_test_reduced = pca.transform(user_feat_df)
    ##selecting classifier
    model = DecisionTreeClassifier(criterion='entropy', max_depth=20, min_samples_split=6)
    # model = LogisticRegression(C=0.1, max_iter=200, penalty='l2', solver='liblinear')
    # model = KNeighborsClassifier(leaf_size=20, n_neighbors=3)
    # model = RandomForestClassifier()
    # model = GaussianNB()
    # model = SVC()
    ##predict label based on non reduced data
    ovr_classifier = OneVsRestClassifier(model)
    ovr_classifier.fit(X_train, y_train)
    predicted = ovr_classifier.predict(user_feat_df)
    ##predict label based on reduced features
    # ovr_classifier.fit(X_train_reduced, y_train)
    # predicted = ovr_classifier.predict(X_test_reduced)
    return (features[predicted])


feats = ['blister', 'red_sore_around_nose', 'yellow_crust_ooze']
result = trained_model_prediction(feats)
print(result[0])

def symptoms():
    df = pd.read_csv("DataSet.csv")
    symptoms = df.iloc[: , :-1]
    return (symptoms.columns)
