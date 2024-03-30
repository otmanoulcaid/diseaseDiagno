import pandas as pd
from sklearn.model_selection import KFold

# Create a KFold object with 5 splits
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Iterate over each fold
for fold_index, (train_index, test_index) in enumerate(kf.split(X), start=1):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Convert the NumPy arrays to pandas DataFrames
    df_train = pd.DataFrame(X_train, columns=["Feature1", "Feature2", ...])  # Replace "Feature1", "Feature2", ... with your actual feature names
    df_train["Target"] = y_train
    
    df_test = pd.DataFrame(X_test, columns=["Feature1", "Feature2", ...])  # Replace "Feature1", "Feature2", ... with your actual feature names
    df_test["Target"] = y_test
    
    # Save the training and testing data to CSV files
    df_train.to_csv(f"train_fold_{fold_index}.csv", index=False)
    df_test.to_csv(f"test_fold_{fold_index}.csv", index=False)
