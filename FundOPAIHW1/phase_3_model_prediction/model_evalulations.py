import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load the metrics from CSV
metrics_df = pd.read_csv('model_training_metrics.csv')

# Plot the distribution of MAE, RMSE, and R2 scores across repetitions
plt.figure(figsize=(15, 5))

# Plot MAE
plt.subplot(1, 3, 1)
plt.hist(metrics_df['MAE'], bins=20, color='skyblue', edgecolor='black')
plt.title('MAE Distribution')
plt.xlabel('MAE')
plt.ylabel('Frequency')

# Plot RMSE
plt.subplot(1, 3, 2)
plt.hist(metrics_df['RMSE'], bins=20, color='lightgreen', edgecolor='black')
plt.title('RMSE Distribution')
plt.xlabel('RMSE')
plt.ylabel('Frequency')

# Plot R2
plt.subplot(1, 3, 3)
plt.hist(metrics_df['R2'], bins=20, color='salmon', edgecolor='black')
plt.title('R2 Distribution')
plt.xlabel('R2')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Load the last test dataset and model for prediction analysis (optional if saved previously)
with open('tra_X_te.pkl', 'rb') as f:
    tra_X_te = pickle.load(f)

with open('tra_Y_te.pkl', 'rb') as f:
    tra_Y_te = pickle.load(f)

# Convert sparse matrices to dense format and create DataFrames
X_test = pd.DataFrame(tra_X_te[0][0].toarray())  # Testing features
y_test = pd.DataFrame(tra_Y_te[:, 0], columns=['Traffic_Point_1'])  # Testing target

# Retrain the model on shuffled data for a final prediction (or load pre-trained model)
model = LinearRegression()
model.fit(X_test, y_test.values.ravel())  # Train on the full test dataset

# Make final predictions
y_test_pred = model.predict(X_test)

# Final Plot: Actual vs. Predicted values for the last repetition
results_test = pd.DataFrame({'Actual': y_test.values.ravel(), 'Predicted': y_test_pred})

# Scatter Plot: Predicted vs. Actual
plt.figure(figsize=(10, 6))
plt.scatter(results_test['Actual'], results_test['Predicted'], alpha=0.6, color='blue')
plt.plot([results_test['Actual'].min(), results_test['Actual'].max()], 
         [results_test['Actual'].min(), results_test['Actual'].max()], 
         'r--', lw=2, label='Perfect Prediction Line')
plt.title('Predicted vs. Actual Traffic Flow')
plt.xlabel('Actual Traffic Flow')
plt.ylabel('Predicted Traffic Flow')
plt.legend()
plt.grid(True)
plt.show()

# Line Plot: Actual vs. Predicted values
plt.figure(figsize=(14, 7))
plt.plot(results_test['Actual'].values, label='Actual', color='blue', linestyle='-')
plt.plot(results_test['Predicted'].values, label='Predicted', color='red', linestyle='--')
plt.title('Actual vs. Predicted Traffic Flow')
plt.xlabel('Sample Index')
plt.ylabel('Traffic Flow')
plt.legend()
plt.grid(True)
plt.show()

# Prediction for the next input (use last test data)
next_input = X_test.iloc[-1].values.reshape(1, -1)  # Reshape to match input format
next_prediction = model.predict(next_input)

print(f"Predicted traffic flow for the next 15 minutes: {next_prediction[0]:.2f}")
