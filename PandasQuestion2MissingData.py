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


