import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("C:/Users/ipinu/OneDrive/Documents/S.YusufCOS102/week-8/archive/Top-Apps-in-Google-Play.csv")

# Display the first 7 rows of the dataset
print(df.head(7))

# Select the first 3 columns of the dataset
# Assuming the columns are named 'Column1', 'Column2', 'Column3'
selected_columns = df[['App Name', 'App Id', 'Category']]
print(selected_columns.head(7))

# Display only one row and the header of the dataset
print(df.iloc[[0]])
