import numpy as np
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Filter the training data to include only 0s and 1s
x_train_filtered = x_train[np.isin(y_train, [0, 1])]
y_train_filtered = y_train[np.isin(y_train, [0, 1])]

# Filter the test data to include only 0s and 1s
x_test_filtered = x_test[np.isin(y_test, [0, 1])]
y_test_filtered = y_test[np.isin(y_test, [0, 1])]

# Print the shapes to verify
print("Filtered training data shape:", x_train_filtered.shape)
print("Filtered training labels shape:", y_train_filtered.shape)
print("Filtered test data shape:", x_test_filtered.shape)
print("Filtered test labels shape:", y_test_filtered.shape)