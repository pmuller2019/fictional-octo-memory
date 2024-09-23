import pandas as pd
import numpy as np
import pickle

# Load the pickled data
with open('tra_X_tr.pkl', 'rb') as f:
    tra_X_tr = pickle.load(f)

with open('tra_Y_tr.pkl', 'rb') as f:
    tra_Y_tr = pickle.load(f)

with open('tra_X_te.pkl', 'rb') as f:
    tra_X_te = pickle.load(f)

with open('tra_Y_te.pkl', 'rb') as f:
    tra_Y_te = pickle.load(f)

# Assuming tra_X_tr contains sparse matrices, convert to dense DataFrame
# Adjust the indices to extract the relevant features based on data structure
df_tra_X_tr = pd.DataFrame(tra_X_tr[0][0].toarray())  # Adjust as needed
df_tra_Y_tr = pd.DataFrame(tra_Y_tr[:, 0], columns=['Traffic_Point_1'])

# Assuming 'number of lanes' is a feature in tra_X_tr (adjust the column index to match)
# For example, let's say column 5 represents 'number of lanes'
df_tra_X_tr['number_of_lanes'] = df_tra_X_tr.iloc[:, 5]  # Replace 5 with the correct column index

# Combine only the necessary features: hour and number of lanes
# Add 'hour' by creating a timestamp and extracting the hour
df_tra_X_tr['timestamp'] = pd.date_range(start='2023-01-01', periods=len(df_tra_X_tr), freq='15T')
df_tra_X_tr['hour'] = df_tra_X_tr['timestamp'].dt.hour

# Combine the relevant features (hour and number of lanes) with the target variable
df = pd.concat([df_tra_X_tr[['hour', 'number_of_lanes']], df_tra_Y_tr], axis=1)

# Drop NaN values if there are any
df.dropna(inplace=True)

# Save the engineered features to a new CSV for model training
df.to_csv('engineered_features_hours_lanes.csv', index=True)

# Display the first few rows to verify the features
print("Engineered Features (Hours and Number of Lanes):")
print(df.head())

# Testing Data Preparation (Optional)
df_tra_X_te = pd.DataFrame(tra_X_te[0][0].toarray())  # Adjust indices based on actual structure
df_tra_Y_te = pd.DataFrame(tra_Y_te[:, 0], columns=['Traffic_Point_1'])

df_tra_X_te['number_of_lanes'] = df_tra_X_te.iloc[:, 46]  

# Add 'hour' to the test data
df_tra_X_te['timestamp'] = pd.date_range(start='2023-01-01', periods=len(df_tra_X_te), freq='15T')
df_tra_X_te['hour'] = df_tra_X_te['timestamp'].dt.hour

# Combine test features and target
df_test = pd.concat([df_tra_X_te[['hour', 'number_of_lanes']], df_tra_Y_te], axis=1)

# Save testing features for future evaluation
df_test.to_csv('engineered_test_features_hours_lanes.csv', index=False)

# Display test data to verify
print("Test Features (Hours and Number of Lanes):")
print(df_test.head())
