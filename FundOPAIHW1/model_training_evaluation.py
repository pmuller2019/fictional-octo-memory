import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Load data
with open('tra_X_tr.pkl', 'rb') as f:
    tra_X_tr = pickle.load(f)

with open('tra_Y_tr.pkl', 'rb') as f:
    tra_Y_tr = pickle.load(f)

with open('tra_X_te.pkl', 'rb') as f:
    tra_X_te = pickle.load(f)

with open('tra_Y_te.pkl', 'rb') as f:
    tra_Y_te = pickle.load(f)

column_headers = [
    'Traffic_1', 'Traffic_2', 'Traffic_3', 'Traffic_4', 'Traffic_5',
    'Traffic_6', 'Traffic_7', 'Traffic_8', 'Traffic_9', 'Traffic_10',
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
    'Hour_0', 'Hour_1', 'Hour_2', 'Hour_3', 'Hour_4', 'Hour_5', 'Hour_6', 'Hour_7',
    'Hour_8', 'Hour_9', 'Hour_10', 'Hour_11', 'Hour_12', 'Hour_13', 'Hour_14', 'Hour_15',
    'Hour_16', 'Hour_17', 'Hour_18', 'Hour_19', 'Hour_20', 'Hour_21', 'Hour_22', 'Hour_23',
    'Direction_North', 'Direction_South', 'Direction_East', 'Direction_West',
    'Number_of_Lanes', 'Road_Name', 'Extra_Column'
]
# Convert to pandas DataFrames
df_tra_X_tr = pd.DataFrame(tra_X_tr[0][0].toarray(), columns=column_headers)  # Training features
df_tra_Y_tr = pd.DataFrame(tra_Y_tr[:, 0])  # Training target (traffic flow)

# Assuming 'Number_of_Lanes' is the 46th feature
number_of_lanes = df_tra_X_tr['Number_of_Lanes']

# Generate polynomial features including the lane feature
poly = PolynomialFeatures(degree=2)  # Adjust degree as needed
df_poly_features = poly.fit_transform(df_tra_X_tr)

# Initialize lists to store metrics
mae_list = []
mse_list = []
rmse_list = []

# Perform 10 training iterations
for iteration in range(10):
    # Randomly sample a subset of the training data
    sample_size = int(len(df_tra_X_tr) * 0.8)  # Using 80% of the data for training
    sampled_indices = np.random.choice(df_tra_X_tr.index, size=sample_size, replace=False)
    
    sampled_X = df_tra_X_tr.loc[sampled_indices]
    sampled_Y = df_tra_Y_tr.loc[sampled_indices]

    # Generate polynomial features for the sampled data
    sampled_poly_features = poly.transform(sampled_X)

    # Train the Linear Regression model using the sampled training data
    lr_model = LinearRegression()
    lr_model.fit(sampled_poly_features, sampled_Y)

    # Convert test data to pandas DataFrames
    df_tra_X_te = pd.DataFrame(tra_X_te[0][0].toarray(), columns=column_headers)  # Test features
    df_tra_Y_te = pd.DataFrame(tra_Y_te[:, 0])  # Test target (traffic flow)

    # Generate polynomial features for the test set
    df_poly_features_te = poly.transform(df_tra_X_te)

    # Make predictions on the test set
    y_pred = lr_model.predict(df_poly_features_te)

    # Evaluate the model's performance using the test set
    mae = mean_absolute_error(df_tra_Y_te, y_pred)
    mse = mean_squared_error(df_tra_Y_te, y_pred)
    rmse = np.sqrt(mse)

    # Store the metrics
    mae_list.append(mae)
    mse_list.append(mse)
    rmse_list.append(rmse)

    print(f"Iteration {iteration + 1}:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}\n")

# Calculate and print average performance metrics over all iterations
print("Average Performance Metrics Over All Iterations:")
print(f"Mean Absolute Error (MAE): {np.mean(mae_list)}")
print(f"Mean Squared Error (MSE): {np.mean(mse_list)}")
print(f"Root Mean Squared Error (RMSE): {np.mean(rmse_list)}\n")

# Visualize actual vs predicted traffic flow for the last iteration
plt.figure(figsize=(10, 5))
plt.plot(df_tra_Y_te.reset_index(drop=True), label='Actual Traffic Flow', alpha=0.7)
plt.plot(y_pred, label='Predicted Traffic Flow', alpha=0.7, linestyle='dashed')
plt.title("Actual vs Predicted Traffic Flow (Test Set - Last Iteration)")
plt.xlabel("Time (15-minute intervals)")
plt.ylabel("Traffic Flow")
plt.legend()
plt.grid()
plt.show()

# Add prediction for the next 15 minutes
next_15_min_pred = lr_model.predict(df_poly_features_te[-1].reshape(1, -1))
print(f"Predicted Traffic Flow for Next 15 Minutes: {next_15_min_pred[0][0]}")
