import pandas as pd

# Define the data for Cadbury Nigeria Plc's products and brands
data = {
    'Segment': ['Refreshment Beverages', 'Confectionery', 'Intermediate Cocoa Products'],
    'Brands': [
        ['CADBURY BOURNVITA', 'CADBURY 3-in-1 HOT CHOCOLATE'],
        ['TOMTOM CLASSIC', 'TOMTOM STRAWBERRY', 'BUTTERMINT'],
        ['COCOA POWDER', 'COCOA BUTTER']
    ],
    'Products': [
        ['Bournvita', 'Hot Chocolate'],
        ['Tom Tom', 'Buttermint'],
        ['Cocoa Powder', 'Cocoa Butter', 'Cocoa Liquor', 'Cocoa Cake']
    ],
    'Export': [
        ['Local Market'],
        ['Local Market'],
        ['International Customers', 'Local Market']
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Explode the lists in 'Brands' and 'Products' columns to have individual rows for each brand/product
df = df.explode('Brands').reset_index(drop=True)
df = df.explode('Products').reset_index(drop=True)
df = df.explode('Export').reset_index(drop=True)

# Save the DataFrame to a CSV file
df.to_csv('cadbury_market.csv', index=False)

print("The cadbury_market.csv file has been created successfully.")
