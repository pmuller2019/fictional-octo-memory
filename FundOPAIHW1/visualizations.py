import pandas as pd
import pickle
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns

# Load the training data from the pickle files
with open('tra_X_tr.pkl', 'rb') as f:
    tra_X_tr = pickle.load(f)
with open('tra_Y_tr.pkl', 'rb') as f:
    tra_Y_tr = pickle.load(f)

# Convert data to pandas DataFrame for easier manipulation
df_tra_X_tr = pd.DataFrame(tra_X_tr[0][0].toarray())  # Convert sparse matrix to dense
df_tra_Y_tr = pd.DataFrame(tra_Y_tr)
# Step 1: Visualize Traffic Flow Over Time for Multiple Locations
num_locations = df_tra_Y_tr.shape[0]

# Step 1: Visualize Traffic Flow Over Time for Available Locations
plt.figure(figsize=(12, 6))
for location_index in range(num_locations):
    traffic_flow_series = df_tra_Y_tr.iloc[:, location_index]
    plt.plot(traffic_flow_series, label=f'Location {location_index + 1}')
plt.title("Traffic Flow Over Time for Locations")
plt.xlabel("Time (15-minute intervals)")
plt.ylabel("Traffic Flow")
plt.legend()
plt.grid()
plt.show()

# Step 2: Autocorrelation and Partial Autocorrelation for Each Location
# ACF Overlay
plt.figure(figsize=(12, 6))
for location_index in range(num_locations):
    traffic_flow_series = df_tra_Y_tr.iloc[location_index].values  # Use .values for a 1D array
    plot_acf(traffic_flow_series, lags=35, ax=plt.gca(), alpha=0.1)  # Use current axis
plt.title("ACF for All Locations")
plt.xlabel("Lags")
plt.ylabel("ACF")
plt.grid()
plt.show()

# PACF Overlay
plt.figure(figsize=(12, 6))
for location_index in range(num_locations):
    traffic_flow_series = df_tra_Y_tr.iloc[location_index].values  # Use .values for a 1D array
    plot_pacf(traffic_flow_series, lags=15, ax=plt.gca(), alpha=0.1)  # Use current axis
plt.title("PACF for All Locations")
plt.xlabel("Lags")
plt.ylabel("PACF")
plt.grid()
plt.show()

# Step 3: Histogram of Traffic Flow for Each Location
plt.figure(figsize=(12, 6))
for location_index in range(num_locations):
    plt.hist(df_tra_Y_tr.iloc[location_index, :], bins=30, alpha=0.5, label=f'Location {location_index + 1}')

plt.title("Histogram of Traffic Volume for Each Location")
plt.xlabel("Flow")
plt.ylabel("Traffic Volume")
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.grid()
plt.show()

# Step 4: Scatter Plot to Compare Traffic Flow vs Time for Each Location
plt.figure(figsize=(12, 6))
for location_index in range(num_locations):
    traffic_flow_series = df_tra_Y_tr.iloc[location_index, :]
    plt.scatter(range(len(traffic_flow_series)), traffic_flow_series, alpha=0.5, label=f'Location {location_index + 1}')

plt.title("Scatter Plot of Traffic Volume for Each Location Over Time")
plt.xlabel("Time (15-minute intervals)")
plt.ylabel("Traffic Volume")
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.grid()
plt.show()
