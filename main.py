import pandas as pd

#  Load data
df = pd.read_csv('raw_data.csv')

print("Original Data:")
print(df)

#  Remove duplicate rows
df = df.drop_duplicates()

#  Fill missing values
df['Customer_Name'] = df['Customer_Name'].fillna('Unknown')
df['Quantity'] = df['Quantity'].fillna(1)
df['Price'] = df['Price'].fillna(0)
df['City'] = df['City'].fillna('Not Available')

#  Create new column (Total Price)
df['Total'] = df['Quantity'] * df['Price']

#  Show cleaned data
print("\nCleaned Data:")
print(df)

#  Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

print("\nCleaned file saved as cleaned_data.csv")