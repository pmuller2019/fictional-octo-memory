import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pickle
from sklearn.utils import shuffle

# Load the pickled training and testing data
with open('tra_X_tr.pkl', 'rb') as f:
    tra_X_tr = pickle.load(f)

with open('tra_Y_tr.pkl', 'rb') as f:
    tra_Y_tr = pickle.load(f)

with open('tra_X_te.pkl', 'rb') as f:
    tra_X_te = pickle.load(f)

with open('tra_Y_te.pkl', 'rb') as f:
    tra_Y_te = pickle.load(f)

# Convert sparse matrices to dense format and create DataFrames
X_train = pd.DataFrame(tra_X_tr[0][0].toarray())  # Training features
y_train = pd.DataFrame(tra_Y_tr[:, 0], columns=['Traffic_Point_1'])  # Training target

X_test = pd.DataFrame(tra_X_te[0][0].toarray())  # Testing features
y_test = pd.DataFrame(tra_Y_te[:, 0], columns=['Traffic_Point_1'])  # Testing target

# Combine all data into one DataFrame
X_combined = pd.concat([X_train, X_test], ignore_index=True)
y_combined = pd.concat([y_train, y_test], ignore_index=True)

# Initialize variables to store metrics for each repetition
mae_list = []
rmse_list = []
r2_list = []

# Perform 100 training repetitions with randomized data
for rep in range(1, 1001):
    # Shuffle the combined data
    X_shuffled, y_shuffled = shuffle(X_combined, y_combined, random_state=rep)

    # Split into new training and testing sets (e.g., 80% training, 20% testing)
    split_index = int(0.8 * len(X_shuffled))
    X_train_new = X_shuffled[:split_index]
    y_train_new = y_shuffled[:split_index]
    X_test_new = X_shuffled[split_index:]
    y_test_new = y_shuffled[split_index:]

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train_new, y_train_new.values.ravel())  # Flatten target for training

    # Make predictions on the testing set
    y_test_pred = model.predict(X_test_new)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test_new, y_test_pred)
    rmse = np.sqrt(mean_squared_error(y_test_new, y_test_pred))
    r2 = model.score(X_test_new, y_test_new)

    # Store the metrics
    mae_list.append(mae)
    rmse_list.append(rmse)
    r2_list.append(r2)

    # Print metrics for each repetition
    print(f"Repetition {rep}: MAE = {mae:.2f}, RMSE = {rmse:.2f}, R2 = {r2:.2f}")

# Convert metrics lists to DataFrame for further analysis
metrics_df = pd.DataFrame({
    'Repetition': range(1, 1001),
    'MAE': mae_list,
    'RMSE': rmse_list,
    'R2': r2_list
})

# Save metrics to a CSV file for analysis
metrics_df.to_csv('model_training_metrics.csv', index=False)
