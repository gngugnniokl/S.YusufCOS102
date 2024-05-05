import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("C:/Users/ipinu/OneDrive/Documents/S.YusufCOS102/week-8/archive (2)/BTC_DATA_V3.0.csv")
# Display the first 7 rows of the dataset
print(df.head(7))

# Select the first 3 columns of the dataset
# Replace 'Week', 'Python', 'Java' with the actual first three column names from your dataset
selected_columns = df.iloc[:, :3]
print(selected_columns.head(7))

# Display only one row and the header of the dataset
# This will display the first row along with the column headers
print(df.iloc[[0]])