import pandas as pd

# Create a DataFrame with missing values (None)
df = pd.DataFrame({
    "A": [1, 2, None, 4, 5],
    "B": [5, 4, 3, 2, None],
    "C": [6, None, 8, 9, 10]
})

# Fill missing values with the mean of each column
df_filled = df.fillna(df.mean())

print(df_filled)

# This will output:
#      A    B      C
# 0  1.0  5.0   6.00
# 1  2.0  4.0   8.25
# 2  3.0  3.0   8.00
# 3  4.0  2.0   9.00
# 4  5.0  3.5  10.00

