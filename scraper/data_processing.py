import pandas as pd

# Load the dataset
df = pd.read_csv('data.csv')

# Check column names
print("Columns in the dataset:", df.columns)

# Standardize column names to remove any leading/trailing spaces
df.columns = df.columns.str.strip()

# Ensure that "stipend" and "location" columns are present
if 'stipend' in df.columns and 'location' in df.columns:
    # Remove rows where the stipend is "Unpaid" (case-insensitive)
    df = df[~df['stipend'].str.strip().str.lower().eq('unpaid')]

    # Keep only rows where the location includes "Hyderabad" (case-insensitive)
    # df = df[df['location'].str.contains("Hyderabad", case=False, na=False)]

    # Overwrite the original CSV file with the filtered data
    df.to_csv('data.csv', index=False)
    print("Filtered data saved back to data.csv")
else:
    print("The required columns 'stipend' or 'location' are missing in the CSV file.")
