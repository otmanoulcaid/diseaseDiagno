import numpy as np

class LinearRegressionCustom:
    def __init__(self, learning_rate=0.01, num_epochs=1000):
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        for _ in range(self.num_epochs):
            # Forward pass
            predictions = np.dot(X, self.weights) + self.bias

            # Compute gradients
            dW = np.dot(X.T, (predictions - y)) / num_samples
            db = np.sum(predictions - y) / num_samples

            # Update weights and bias
            self.weights -= self.learning_rate * dW
            self.bias -= self.lea rning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Example usage:
# Assuming X and y are your feature matrix and target vector, respectively

# Instantiate the model
model = LinearRegressionCustom(learning_rate=0.01, num_epochs=1000)

# Train the model
model.fit(X, y)

# Predict
predictions = model.predict(X)

# Optionally, print weights and bias
print("Weights:", model.weights)
print("Bias:", model.bias)
