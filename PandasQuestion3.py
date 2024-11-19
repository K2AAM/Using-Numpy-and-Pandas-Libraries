import pandas as pd

# Create a dictionary with product data
data = {'Product': ['A', 'B', 'C', 'D'],
        'Price': [10, 20, 30, 40],
        'Quantity': [2, 5, 1, 3]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Calculate the total cost for each product and store it in a new column 'Total'
df['Total'] = df['Price'] * df['Quantity']

# Print the DataFrame
print(df)

# This will output:
#   Product  Price  Quantity  Total
#0       A     10         2     20
#1       B     20         5    100
#2       C     30         1     30
#3       D     40         3    120
